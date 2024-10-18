# SYN Flooding Tool
## Start SYN packet flooding:

### Prerequisite:
Take a Linux machine which will act as server and target machine to be flooded with SYN packets. The client machine should be reachable to the server.

### Steps:
1) Pull this tool on a Linux machine:
   
  ```bash
  $> git clone https://github.com/gangaram-tii/ghaf-debug-tools.git
  $> cd ./ghaf-debug-tools/syn-flooding/ 
  ```

2) Setup Nix Shell (For NixOS based Linux machine)

  ```bash
  $> nix-shell
  ```

3) Run following script to measure network performance.
   Modify target ip and port in the script and run it.

   ```bash
   $> sudo python ./start-syn-flooding.py
   ```

