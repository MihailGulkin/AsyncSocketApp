import dataclasses
import socket
import asyncio
from abc import ABC, abstractmethod


@dataclasses.dataclass
class Address:
    host: str
    port: int


@dataclasses.dataclass
class AcceptedClient:
    client_socket: socket
    client_address: Address


class BaseSocket(ABC):
    @abstractmethod
    def __init__(self, address: Address):
        self._address = address
        self.server_socket = self._configurate_socket()

    @abstractmethod
    def _configurate_socket(self) -> socket:
        pass


class SocketConfigurate(BaseSocket):
    def __init__(self, address: Address):
        super().__init__(address)
        self.clients: list[AcceptedClient] = []

    def _configurate_socket(self) -> socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self._address.host, self._address.port))
        server_socket.listen(5)
        return server_socket

    def accept(self):
        client_socket, client_address = self.server_socket.accept()
        self.clients.append(AcceptedClient(
            client_socket=client_socket,
            client_address=client_address)
        )
        print(f"Client connected from {self.clients[-1].client_address}")

    async def handle_client(self) -> None:
        client = self.clients.pop()
        request = client.client_socket.recv(1024)
        print(f'Request from client {request}')
        response = b"Hello, client!"
        client.client_socket.send(response)
        client.client_socket.close()


async def run_server():
    print("Server is running on localhost:8000")
    address = Address('localhost', 8000)
    socket_config = SocketConfigurate(address)

    while True:
        socket_config.accept()
        await socket_config.handle_client()


def main():
    asyncio.run(run_server())


if __name__ == '__main__':
    main()
