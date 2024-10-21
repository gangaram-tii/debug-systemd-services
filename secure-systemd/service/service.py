import time
import os
import sh
import re
from datetime import datetime
from .debug import trace
from .configs import serviceconfigs
from .optimizer import OptionEvaluator, OptimalOptionsSelector
from .capabilities import linuxcaps
from .systemcalls import syscallgroups
from .extraconfigs import extraconfs

Suspects = ["error", "failed", "permission", "allowed", "alert", "warning", "could not", "no such device", "not support" ]

def formatted_time_now() -> str:
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

class SystemdService:
    def __init__(self, service, residue, interactive, latency):
        self.service = service
        self.residue = residue
        self.latency = latency
        self.interactive = interactive
        self.since = "2050"
        self.hardenedconfigs = []
        override_dir = f"/run/systemd/system/{service}.d"
        # Config override file
        self.config_path = os.path.join(override_dir, "override.conf")
        self.reset()
        self.reference_log, self.reference_stats = self.log_stats()
        # Default configs for the service
        self.initial_configs = sh.systemctl("cat", service).splitlines()
        sh.sudo("mkdir", "-p", override_dir)

        trace("=============Reference Start================")
        trace(self.reference_log, "\n", self.reference_stats)
        trace("=============Reference Stop=================")

    def mutable(self, config):
        for line in self.initial_configs:
            if config in line:
                trace(f"Found in initial config: {line.strip()}")
                return False, line.strip()
        return True, None

    def is_active(self):
        try:
            res = sh.systemctl('is-active', self.service)
            return res.strip() == 'active'
        except sh.ErrorReturnCode as e:
            return False

    def log_stats(self):
        log = sh.sudo("journalctl", "-b", "0", "-u", f"{self.service}", "--since", self.since)
        logstats = {}

        if "-- No entries --" in log:
            raise ValueError("Error! Couldn't retrieve service log.")

        for err in Suspects:
            matches = re.findall(err, log, re.IGNORECASE)
            logstats[err] = len(matches)
        return log, logstats

    def log(self):
        msg = sh.sudo("journalctl", "-b", "0", "--since", self.since)

        if "-- No entries --" in msg:
            raise ValueError("Error! Couldn't retrieve service log.")

        return msg


    def log_stats_ok(self, stats):
        for err in Suspects:
            if stats[err] > self.reference_stats[err]:
                trace(f"{err}:This[{stats[err]}] - Ref[{self.reference_stats[err]}]")
                return False
        return True

    def start(self):
        return sh.sudo('systemctl', 'start', self.service)

    def stop_service(self):
        return sh.sudo('systemctl', 'stop', self.service)

    def reload(self):
        try:
            sh.sudo('systemctl', 'daemon-reload')

            if self.is_active():
                sh.sudo('systemctl', 'stop', self.service)
                time.sleep(self.latency)

            self.since = formatted_time_now()
            sh.sudo('systemctl', 'start', self.service)
            time.sleep(self.latency)
            return True

        except sh.ErrorReturnCode as e:
            return False

    def reset(self):
        if self.residue != "":
            sh.sudo("rm", "-rf", self.residue)
        sh.sudo("rm", "-rf", self.config_path)
        return self.reload()

    def get_name(self) -> str:
        return self.service

    def get_config_path(self) -> str:
        return self.config_path

    def get_exposure(self) -> float:
        out = sh.systemd_analyze("security", self.service)
        lines = out.splitlines()
        # Get the last line
        last_line = lines[-1] if lines else None
        match = re.search(r"(\d+\.\d+)", last_line)
        if match:
            number = match.group(1)
            return float(number)
        else:
            return float(-1.0)

    def check_configs(self, configs) -> bool:
        with open(self.get_config_path(), 'w') as file:
            file.write(configs)

        if self.reload() == False:
            if self.reset() == False:
                raise ValueError("Critical Error - 1!")
            return False

        _log, stats = self.log_stats()
        if self.log_stats_ok(stats) == False:
            trace("\n===============Start===============")
            trace(_log, "\n", stats)
            trace("\n===============Stop===============")
            time.sleep(3)
            if self.reset() == False:
                print(self.log())
                raise ValueError("Critical Error - 2!")
            return False

        if self.is_active():
            ok = 'y'
            if self.interactive == True:
                ok = ""
                while ok != "y" and ok != "n":
                    ok = input("Service status. OK?(y/n):").lower()
            if ok == 'y':
                return True
            else:
                return False
        else:
            if self.reset() == False:
                raise ValueError("Critical Error - 3!")
            return False

    def get_hardened_configs(self, reconfig = False):
        if len(self.hardenedconfigs) > 0 and reconfig == False:
            return self.hardenedconfigs
        base = OptionEvaluator(self, serviceconfigs)
        baseconfigs = base.hardened(True)
        optimalcaps = OptimalOptionsSelector(self, baseconfigs, "CapabilityBoundingSet", linuxcaps)
        hardenedconf0 = optimalcaps.hardened(minimal=[""])
        optimalsyscalls = OptimalOptionsSelector(self, hardenedconf0, "SystemCallFilter", syscallgroups)
        hardenedconf = optimalsyscalls.hardened()
        for conf, options in extraconfs.items():
            inputconfs = hardenedconf[:]
            configoptimizer = OptimalOptionsSelector(self, inputconfs, conf, options)
            hardenedconf = configoptimizer.hardened()
        return hardenedconf
