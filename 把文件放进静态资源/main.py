import uvicorn
from pathlib import Path

from lika.server import Server, RouterPath
from lika.response import Response


port = 8080
server = Server()

root = server.router_map


@root.router("/root")
async def _(scope, receive):
    print(root)
    return Response(200)


# 添加服务器位置
@root.router("/command")
async def _(scope, receive):
    if scope["client"][0] != "127.0.0.1":
        return Response(401)
    request = await receive()
    command: str = request["body"].decode()
    command = command.strip().split()
    if len(command) != 2:
        return Response(400)
    do, url = command
    url = "src" + RouterPath(url)
    if do == "del":
        parent = root.get_map(url[:-1])
        if parent and url[-1] in parent:
            del parent[url[-1]]
            return Response(200)
        return Response(418)
    root.set_map(url).file_for_router(Path(do))
    return Response(200)


uvicorn.run(server, host="0.0.0.0", port=port)
