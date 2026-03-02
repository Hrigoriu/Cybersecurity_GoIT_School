import platform

import aiohttp
import asyncio


async def main():

    session = aiohttp.ClientSession()
    response = await session.get("https://python.org")

    print("Status:", response.status)
    print("Content-type:", response.headers["content-type"])

    html = await response.text()
    response.close()

    await session.close()
    return f"Body: {html[:15]}..."


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)

"""
Status: 200
Content-type: text/html; charset=utf-8
Body: <!doctype html>...
"""
# =============================================================================================
import platform

import aiohttp
import asyncio


async def index(session):
    url = "https://python.org"
    async with session.get(url) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers["content-type"])

        html = await response.text()
        return f"Body: {html[:15]}..."


async def doc(session):
    url = "https://www.python.org/doc/"
    async with session.get(url) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers["content-type"])

        html = await response.text()
        return f"Body: {html[:15]}..."


async def main():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(index(session), doc(session))
        return result


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)

"""
Status: 200
Content-type: text/html; charset=utf-8
Status: 200
Content-type: text/html; charset=utf-8
['Body: <!doctype html>...', 'Body: <!doctype html>...']
"""
# =============================================================================================
import platform

import aiohttp
import asyncio
from uuid import uuid4


async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(
        headers={"Request-Id": str(uuid4())},
        timeout=timeout,
    ) as session:
        async with session.get("https://python.org") as response:

            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])

            html = await response.text()
            return f"Body: {html[:15]}..."


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)

"""
Status: 200
Content-type: text/html; charset=utf-8
Body: <!doctype html>...
"""
# =============================================================================================
# =============================================================================================
# Web-сервер
from http.server import HTTPServer, BaseHTTPRequestHandler


class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        data = self.rfile.read(int(self.headers["Content-Length"]))
        print(data)
        self.send_response(201)
        self.end_headers()
        self.wfile.write(b"Done request!" + data)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, world!")


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ("", 5000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    run()

# =============================================================================================
# клієнт
import platform

import aiohttp
import asyncio
from uuid import uuid4


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://localhost:5000", data={"message": "Hello world!"}, ssl=False
        ) as response:

            print("Status:", response.status)
            html = await response.text()
            return f"Body: {html}"


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)

"""
127.0.0.1 - - [25/Feb/2026 23:21:33] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [25/Feb/2026 23:21:37] "GET /favicon.ico HTTP/1.1" 200 -
"""
# =============================================================================================
