import httpx

url = "http://127.0.0.1:8080/command"
file = "C:\\Users\\karis\\Videos\\Captures\\Noita - Build Jan 25 2025 - 15_55_41 2025-05-09 20-58-47.mp4"
net_path = "Noita - Build Jan 25 2025 - 15_55_41 2025-05-09 20-58-47.mp4"  # 网络路径不建议用中文因为还得转码

httpx.post(url, data=f"{file} {net_path}".encode())
input("wait")
httpx.post(url, data=f"del {net_path}".encode())
