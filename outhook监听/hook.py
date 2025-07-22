import socket

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def callback(line: bytes) -> None:
    udp_client.sendto(line, ("localhost", 11005))
