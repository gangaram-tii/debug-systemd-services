# Systemd
## Syscall filtering of a systemd service using audit tool:
### Build platform:
1) Go to your 'Ghaf' root.
2) Pull this tool:

   ```bash
   $> curl -L https://github.com/gangaram-tii/ghaf-debug-tools/archive/refs/heads/main.zip --output ghaf-debug-tools-main.zip && unzip ghaf-debug-tools-main.zip
   ```
  or

  ```
  $> git clone https://github.com/gangaram-tii/ghaf-debug-tools.git
  ```

3) Find the service binary path from `/etc/systemd/system/<service-name>.service` on Ghaf host/vm.

   ```bash
   $> cat /etc/systemd/system/<service-name>.service | grep -oP '^ExecStart=\s*\K\S+'
   ```

   From the path, identify package name.


4) Apply the patch for the service binary and use a service tag, which will be used to filter the service log from audit log. Handle escape sequence when specifying the path.

   ```bash
   $> ./ghaf-debug-tools<-main>/systemd/build-system/patch-ghaf.sh "<absolute-service-path>" "<service-tag>"
   $> #Example of 'alloy' service
   $> ./ghaf-debug-tools<-main>/systemd/build-system/patch-ghaf.sh "\${pkgs.grafana-alloy}\/bin\/alloy" "alloy-tag"
   ```

5) Build and load the Ghaf for the target.

### Ghaf Host/VM:
1) Pull Ghaf debug tools to a local directory. (Build platform:Step(2))
2) Run following script to filter the system calls.

   ```bash
   $> sudo ./ghaf-debug-tools<-main>/systemd/host/extract-syscalls.sh "<service-tag>"
   ```
   This will list system calls made by the service main and child process as well.
   It will also list access of syscall groups required by the service.(TODO)
