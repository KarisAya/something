import uvicorn
from pathlib import Path
from lika import Server, RoutePath, Response
from lika.router import RoutePathError

server = Server()
root = server.route_map


# 添加服务器位置
@root.router("/command")
async def _(scope, receive):
    if scope["client"][0] != "127.0.0.1":
        return Response(401, [(b"Content-type", b"text/plain")], [b"Permission denied"])
    request = await receive()
    command: str = request["body"].decode()
    command_list = command.strip().split(maxsplit=2)
    if len(command_list) != 2:
        return Response(400, [(b"Content-type", b"text/plain")], [f"{command_list} is not a command".encode(encoding="utf-8")])
    do, url = command_list
    url = "sample" + RoutePath(url)
    if do == "del":
        try:
            del root.find_route(url[:-1])[url[-1]]
            return Response(200)
        except RoutePathError | KeyError:
            return Response(400, [(b"Content-type", b"text/plain")], [f"{url.url} are not exist"])
    try:
        path = Path(do)
    except ValueError:
        return Response(400, [(b"Content-type", b"text/plain")], [f"{do} are not a path"])
    if not path.exists():
        return Response(400, [(b"Content-type", b"text/plain")], [f"{do} are not exist"])
    root.create_route(url).file_for_router(path)
    return Response(200)


uvicorn.run(server, host="0.0.0.0", port=8080)
