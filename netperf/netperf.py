import subprocess
import json
import paramiko
import socket

def run_iperf3_client_new(server_ip, remote_ip, duration=10, username=None, password=None, logdir="/tmp"):
    """Run iperf3 client on the remote machine."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remotelogfile = f'/tmp/iperf3/iperf3-{remote_ip}-log.txt'
    # Connect to the remote server
    client.connect(remote_ip, username=username, password=password)

    # Execute the command
    stdin, stdout, stderr = client.exec_command(f'rm -rf /tmp/iperf3')
    stdin, stdout, stderr = client.exec_command(f'mkdir /tmp/iperf3')
    # Wait for the command to complete
    exitst = stdout.channel.recv_exit_status()
    if exitst == 1:
        print(f"Failed to create file in /tmp on remote machine")
        exit(1)

    # Construct the iperf3 command
    iperf_command = f'iperf3 -c {server_ip} -t {duration} -J --logfile {remotelogfile}'
    stdin, stdout, stderr = client.exec_command(iperf_command)

    # Wait for the command to complete
    exitst = stdout.channel.recv_exit_status()
    if exitst == 1:
        print(f"Failed to run iperf3 on remote machine.")
        exit(1)

    stdin, stdout, stderr = client.exec_command(iperf_command)

    # Wait for the command to complete
    exitst = stdout.channel.recv_exit_status()
    if exitst == 1:
        print(f"Failed to run iperf3 on remote machine.")
        exit(1)

    try:
        ssh = create_ssh_client(server, user, password)
        with SCPClient(client.get_transport()) as scp:
            scp.get(remotelogfile, logdir)
    except SCPException as e:
        print(f"SCP error: {e}")


    # Wait for the command to complete
    exitst = stdout.channel.recv_exit_status()
    if exitst == 1:
        print(f"Failed to run iperf3 on remote machine.")
        exit(1)


    # Close the SSH client
    client.close()

    # Parse JSON output
    #return json.loads(output)
    return output


def get_local_ip():
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        my_local_ip = s.getsockname()[0]
    except Exception as e:
        print(f"Error occurred: {e}")
        my_local_ip = None
    finally:
        if s is not None:
            s.close()
    return my_local_ip

def run_iperf3_client(server_ip, duration=10, parallel_streams=1):
    """Run iperf3 client locally and return parsed JSON output."""
    command = [
        'iperf3', '-c', server_ip, '-t', str(duration), '-P', str(parallel_streams), '-J'
    ]

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    # Check for errors
    if result.returncode != 0:
        print("Error running iperf3:", result.stderr)
        return None

    # Parse JSON output
    return json.loads(result.stdout)

if __name__ == "__main__":
    server_ip = "SERVER_IP"  # Replace with the IP address of the remote iperf3 server
    duration = 10              # Test duration in seconds
    parallel_streams = 1      # Number of parallel streams

    data = run_iperf3_client_new(get_local_ip(), "192.168.1.131", "ghaf","ghaf")
    # Run iperf3 client on the server machine
    #data = run_iperf3_client(server_ip, duration, parallel_streams)
    if data:
        #print("iperf3 results:", json.dumps(data, indent=4))
        print("iperf3 results:", data)
