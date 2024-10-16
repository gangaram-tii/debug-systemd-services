# Audit
## Network subsystem hardening using sysctl:
1) Pull this tool on the **Ghaf** machine on netvm(or copy to any target vm):

   ```bash
   $> curl -L https://github.com/gangaram-tii/ghaf-debug-tools/archive/refs/heads/main.zip --output ghaf-debug-tools-main.zip && unzip ghaf-debug-tools-main.zip
   ```
  or

  ```
  $> git clone https://github.com/gangaram-tii/ghaf-debug-tools.git
  ```

2) Run following script to generate the audit report.

   ```bash
   $> sudo ./ghaf-debug-tools<-main>/audit/sysctl/network/run_audit.sh
   ```
   This will generate audit report md file `sysctl_network_audit_report.md` in current working directory.
