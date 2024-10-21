#!.venv/bin/python
import os
from service.service import SystemdService
import sys
import argparse
import service.debug as debug


def check_sudo():
    if os.geteuid() != 0:
        print("This program must be run as root (use sudo).")
        sys.exit(1)

def get_exposure_emoji(exposure :float) -> str:
    exposure_emoji = {8.5:"[UNSAFE] 😨", 7.0:"[EXPOSED] 🙁", 5.0:"[MEDIUM] 😐", 0.1:"[SAFE] 🙂" }
    for key in sorted(exposure_emoji.keys(), reverse=True):
        if exposure > key:
            return exposure_emoji[key]

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate hardened configuration for systemd service.')
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('service', type=str, help='Name of the service')
    group.add_argument('-r', '--reset', action='store_true', help='Reset service to default configuration.')
    group.add_argument('-H', '--harden', type=str, help='Output file path to save hardened configuration.')
    parser.add_argument('-R', '--residue', type=str, help='Service residues to clear before service restart.', default="")
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable logs.')
    parser.add_argument('-l', '--latency', type=int, help='Service latency in seconds to wait after service start/stop.', default=2)
    parser.add_argument('-i', '--interactive', action='store_true', help='Enable interactive mode.')

    # Parse the command-line arguments
    args = parser.parse_args()

    check_sudo()

    if args.verbose == True:
        debug.enable_traces()

    service = SystemdService(service=args.service,
                            residue=args.residue,
                            interactive=args.interactive,
                            latency = args.latency)

    if args.reset == True:
        if service.reset() == False:
            print("Failed to reset the service.")
            sys.exit(1)
        else:
            print("The service is reset to it's default config.")
            sys.exit(0)

    if args.harden == "":
        print("Output file path is missing.")
        sys.exit(1)

    old_exposure = service.get_exposure()
    hardened_configs = service.get_hardened_configs()
    print(hardened_configs)
    configs = "\n".join(hardened_configs)
    with open(args.harden, 'w') as file:
        file.write(configs)
    new_exposure = service.get_exposure()
    old_emoji = get_exposure_emoji(old_exposure)
    new_emoji = get_exposure_emoji(new_exposure)

    print(f"Exposure level before: {old_exposure}{old_emoji} and after: {new_exposure}{new_emoji}")

if __name__ == "__main__":
    main()
