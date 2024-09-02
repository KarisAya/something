import requests

url = "http://127.0.0.1:8080/command"
file = "C:/Users/karis/Videos/6月22日.mp4"
net_path = "sample/xxx.mp4"  # 网络路径不建议用中文

requests.post(url, data=f"{file} {net_path}".encode())
requests.post(url, data=f"del {net_path}".encode())
