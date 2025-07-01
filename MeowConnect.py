import socket
import argparse
import ipaddress

def send_udp_packet(destination_ip, port, data):
    """Send a UDP packet to the specified address and port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(data, (destination_ip, port))
        print(f"✅ UDP packet sent to {destination_ip}:{port}")
    finally:
        sock.close()

def is_valid_ip(ip_str):
    """Check if the provided IP address is valid."""
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def main():
    # Argument parser with automatic help enabled
    parser = argparse.ArgumentParser(description="UDP Packet Sender")
    parser.add_argument("TargetIP", nargs='?', help="Target IP address (if not provided, you will be prompted)")

    args = parser.parse_args()

    # Get the target IP
    if args.TargetIP:
        DEST_IP = args.TargetIP
    else:
        DEST_IP = input("Please enter the destination IP address: ")

    # Validate the IP format
    if not is_valid_ip(DEST_IP):
        print("❌ Invalid IP address format.")
        return

    # UDP destination port
    DEST_PORT = 49983

    # Data to send (in hexadecimal format)
    DATA_HEX = "66 bd 5a 61 e2 c1 d8 bb c1 fb 35 80 08 00 45 00 00 4f 45 f7 00 00 80 11 00 00 c0 a8 01 04 c0 a8 01 c5 c3 3f c3 3f 00 3b 84 66 69 46 61 63 69 61 6c 4d 6f 63 61 70 5f 73 61 68 75 61 73 6f 75 72 79 79 61 39 32 31 38 73 61 75 68 75 69 61 79 65 74 61 39 31 35 35 35 64 79 33 37 31 39"
    DATA = bytes.fromhex(DATA_HEX)

    # Display the sending parameters
    print(f"🔧 Sending UDP packet to {DEST_IP}:{DEST_PORT}")

    # Send the UDP packet
    send_udp_packet(DEST_IP, DEST_PORT, DATA)

if __name__ == "__main__":
    main()
