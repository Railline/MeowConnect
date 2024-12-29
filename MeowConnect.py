import socket
import argparse

parser = argparse.ArgumentParser(add_help = False)

DEST_IP_ARG = ''
parser.add_argument("TargetIP", help = "Sends the packet to the specified adress",nargs='?')

args = parser.parse_args()


def send_udp_packet(destination_ip, port, data):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Send the packet
        sock.sendto(data, (destination_ip, port))
        print(f"UDP packet sent to {destination_ip}:{port}")
    finally:
        # Close the socket
        sock.close()

if __name__ == "__main__":
    # Ask the user for the destination IP if not described in argument
    if args.TargetIP == None:
        DEST_IP = input("Please enter the destination IP address: ")
    else:
        DEST_IP = args.TargetIP
    # Destination port
    DEST_PORT = 49983
    # Data to send (replace with the desired hexadecimal data)
    # To reproduce the previously provided data, convert the hexadecimal to bytes
    DATA_HEX = "66 bd 5a 61 e2 c1 d8 bb c1 fb 35 80 08 00 45 00 00 4f 45 f7 00 00 80 11 00 00 c0 a8 01 04 c0 a8 01 c5 c3 3f c3 3f 00 3b 84 66 69 46 61 63 69 61 6c 4d 6f 63 61 70 5f 73 61 68 75 61 73 6f 75 72 79 79 61 39 32 31 38 73 61 75 68 75 69 61 79 65 74 61 39 31 35 35 35 64 79 33 37 31 39"
    DATA = bytes.fromhex(DATA_HEX)

    # Send the packet
    send_udp_packet(DEST_IP, DEST_PORT, DATA)
