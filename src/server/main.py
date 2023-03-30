import asyncio

from src.server.server import SocketServerRunner

if __name__ == '__main__':
    asyncio.run(SocketServerRunner.run_server())