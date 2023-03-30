import asyncio

from src.client.client import SocketClientRunner

if __name__ == '__main__':
    asyncio.run(SocketClientRunner.run_server())
