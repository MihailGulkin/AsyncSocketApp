import asyncio

from src.application.client.ports.client import SocketClientRunner
from src.settings import Config

if __name__ == '__main__':
    asyncio.run(SocketClientRunner.run(
        config=Config
    ))
