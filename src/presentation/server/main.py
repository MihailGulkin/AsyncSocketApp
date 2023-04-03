import asyncio

from src.application.server.ports.server import SocketServerRunner
from src.settings import Config

if __name__ == '__main__':
    asyncio.run(SocketServerRunner.run(
        config=Config
    ))
