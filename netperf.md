# Network performance
## Network performance using iperf3:

### Prerequisite:
Take a Linux machine which will act as server and target machine will act as client. The client and server should be in same subnet in order to minimize network latency.

### Steps:
1) Pull this tool on a Linux machine:
   
  ```bash
  $> git clone https://github.com/gangaram-tii/ghaf-debug-tools.git
  $> cd ./ghaf-debug-tools/netperf/ 
  ```

2) Setup Nix Shell (For NixOS based Linux machine)

  ```bash
  $> nix-shell
  ```

3) Run following script to measure network performance.
   The script uses default port (5201). Make sure the port is allowed in firewall setting.

   ```bash
   $> python ./netperf.py <target-ip> <duration-in-sec> <target-username> <target-password>
   ```

   This will generate iperf3 json log on remote machine and will copy the log file in current working directory with name `iperf3-<target-ip>-<datetime>.json.
   You can run multiple such iterations.

4) Draw plot for comparision of any two performance data:

   ```bash
   $> python ./plot.py <perf-log-file1> <label1> <perf-log-file2> <label2>
   ```

   The graph will show bitrates of the two instances overtime using line graph. It will show comparision of average CPU utilization in both instances using bar graph.
