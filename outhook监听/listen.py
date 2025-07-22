import socket


udp_listen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_listen.bind(("localhost", 11005))
while True:
    try:
        data, address = udp_listen.recvfrom(1024)
        print(f"从 {address} 收到消息: {data.decode("utf-8")}", end="")
    except Exception as e:
        print(e)
