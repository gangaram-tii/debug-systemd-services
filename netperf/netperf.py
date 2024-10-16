import subprocess
import paramiko
import socket
import os
import argparse
from scp import SCPClient, SCPException
from datetime import datetime

def run_iperf3_client_new(server_ip, remote_ip, duration=10, username=None, password=None, port=5201):
    """Run iperf3 client on the remote machine."""
    try:
        logdir=os.getcwd()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


        # Get the current time
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Create the filename with the current time
        logfile=f'iperf3-{remote_ip}-{current_time}.json'
        remotelogfile = f'/tmp/iperf3/{logfile}'
        # Connect to the remote server
        client.connect(remote_ip, username=username, password=password)
        # Execute the command
        stdin, stdout, stderr = client.exec_command(f'rm -rf /tmp/iperf3')
        stdin, stdout, stderr = client.exec_command(f'mkdir /tmp/iperf3')
        # Wait for the command to complete
        exitst = stdout.channel.recv_exit_status()
        if exitst == 1:
            raise ValueError("Failed to create file in /tmp on remote machine")
        # Construct the iperf3 command
        iperf_command = f'iperf3 -c {server_ip} -t {duration} -p {port} -J --logfile {remotelogfile}'
        stdin, stdout, stderr = client.exec_command(iperf_command)
        # Wait for the command to complete
        exitst = stdout.channel.recv_exit_status()
        if exitst == 1:
            raise ValueError("Failed to run iperf3 on remote machine.")

    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        with SCPClient(client.get_transport()) as scp:
            scp.get(remotelogfile, logdir)
            print(f'Log file: {logdir}/{logfile}')
    except SCPException as e:
        print(f"SCP error: {e}")


    finally:
        # Close the SSH client
        client.close()

    return


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

def start_iperf_server(port=5201):
    # Command to start iperf server
    command = ['iperf', '-s', '-p', str(port)]

    # Start the server in the background
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return process

def cleanup(process):
    print(f"Terminating iperf server with PID: {process.pid}")
    process.terminate()  # Gracefully terminate the process
    process.wait()       # Wait for the process to terminate


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Run iperf3 on target machine from server and get performance data in current working directory.')
    parser.add_argument('remote_ip', type=str, help='The IP address of the remote iperf3 server')
    parser.add_argument('duration', type=int, help='Test duration in seconds')
    parser.add_argument('username', type=str, help='Username for authentication')
    parser.add_argument('password', type=str, help='Password for authentication')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Start the iperf server and run the client
    iperf3 = start_iperf_server()
    server = get_local_ip()
    run_iperf3_client_new(server_ip=server, remote_ip=args.remote_ip, duration=args.duration, username=args.username, password=args.password)
    cleanup(iperf3)
