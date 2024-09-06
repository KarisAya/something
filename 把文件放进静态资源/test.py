import requests

url = "http://127.0.0.1:8080/command"
file = "C:\\Users\\karis\\Downloads\\涩涩\\0046.mp4"
net_path = "0046.mp4"  # 网络路径不建议用中文

requests.post(url, data=f"{file} {net_path}".encode())
input("wait")
requests.post(url, data=f"del {net_path}".encode())
