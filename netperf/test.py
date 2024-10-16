import socket

def get_local_ip():
    try:
        # Create a socket and connect to an external address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  # Connect to Google's public DNS
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip

if __name__ == "__main__":
    my_local_ip = get_local_ip()
    print(f"My local IP address is: {my_local_ip}")

