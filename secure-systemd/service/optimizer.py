import copy

class OptionEvaluator:
    def __init__(self, service, configs):
        self.service = service
        self.hardenedconfigs = []
        self.configs = configs

    def hardened(self, reconfig = False) -> list[str]:
        if reconfig==False and len(self.hardenedconfigs) > 0:
            return self.hardenedconfigs

        hardenedconfigs = ["[Service]"]
        for conf, possible_values in self.configs.items():
            mutable, config = self.service.mutable(conf)
            if mutable == False:
                #print("\tFound in service config")
                # Initial configs can not be overridden
                hardenedconfigs.append(config)
                print(f"{config}".ljust(50)+"[u]")
                continue
            else:
                for val in possible_values:
                    buffer = "\n".join(hardenedconfigs)
                    buffer += f"\n{conf}={val}"
                    print(f"{conf}={val}".ljust(50), end="")

                    if self.service.check_configs(buffer) == True:
                        hardenedconfigs.append(f"{conf}={val}")
                        print("[✓]")
                        break
                    else:
                        print("[✗]")
        self.hardenedconfigs = hardenedconfigs
        return self.hardenedconfigs

class OptimalOptionsSelector:
    def __init__(self, service, baseconfig, config, values):
        self.service = service
        self.baseconf = copy.deepcopy(baseconfig)
        self.optimalconfigs = []
        self.configoptions = []
        self.config = config
        self.invertedconfigs = (values[0][0] == "~")
        for val in values:
            negval = "~" + val
            mutable, _ = service.mutable(negval)
            if mutable == False:
                self.optimalconfigs.append(f"{config}={negval}")
                print(f"{self.config}={negval}".ljust(50)+ "[u]")
                continue
            mutable, _ = service.mutable(val)
            if mutable == False:
                self.optimalconfigs.append(f"{config}={val}")
                print(f"{self.config}={val}".ljust(50)+ "[u]")
                continue
            self.configoptions.append(f"{config}={val}")

    def hardened(self, minimal=[]) -> list[str]:
        if len(self.optimalconfigs) > 1:
            return self.baseconf + self.optimalconfigs

        if len(minimal) > 0:
            for mini in minimal:
                self.baseconf.append(f"{self.config}={mini}")
                print(f"{self.config}={mini}".ljust(50)+ "[u]")

        while True:
            serviceconf = self.baseconf + self.optimalconfigs
            testconf = self.configoptions.pop()
            confval = testconf.split("=")[1]
            if confval in minimal or confval.replace("~", "") in minimal:
                continue

            if self.invertedconfigs == True:
                serviceconf += [testconf]
            else:
                serviceconf += self.configoptions

            buffer = "\n".join(serviceconf)
            print(f"{testconf}".ljust(50), end="")
            if self.service.check_configs(buffer) == True:
                if self.invertedconfigs == True:
                    self.optimalconfigs.append(testconf)
                    print("[✓]")
                else:
                    print("[✗]")
            else:
                if self.invertedconfigs == False:
                    self.optimalconfigs.append(testconf)
                    print("[✓]")
                else:
                    print("[✗]")

            if len(self.configoptions) == 0:
                break

        return self.baseconf + self.optimalconfigs
