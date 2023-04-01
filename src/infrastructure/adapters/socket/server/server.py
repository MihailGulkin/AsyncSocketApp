import socket

from src.domain.dto import AcceptedClient
from src.domain.interfaces import BaseSocket
from src.infrastructure.adapters.io import SocketIO


class BaseServerSocket:
    def __init__(
            self,
            server: BaseSocket,
            socket_io: SocketIO
    ):
        self.server = server
        self.server_io = socket_io
        self.clients: list[AcceptedClient] = []

    async def _accept(self):
        try:
            client_socket, client_address = self.server.socket.accept()
        except socket.timeout:
            return
        self.clients.append(
            AcceptedClient(
                client_name=f'client_{len(self.clients)}',
                client_socket=client_socket,
                client_address=client_address
            ))
        self.clients[-1].client_socket.settimeout(0.2)
        await self.server_io.socket_output.write_message(
            f"Client connected from {self.clients[-1].client_address}"
        )

    async def _close_all_connections(self):
        for client in self.clients:
            client.client_socket.close()

    async def _send_information_for_clients(self):
        if self.server_io.socket_input.value:
            for client in self.clients:
                client.client_socket.send(
                    self.server_io.socket_input.value.encode()
                )
            await self.server_io.socket_input.run_thread()

    async def _get_information_for_clients(self):
        for client in self.clients:
            try:
                request = client.client_socket.recv(1024).decode()
            except socket.timeout:
                continue

            if not client.is_have_name:
                client.client_name = f'{client.client_name} - {request}'
                client.is_have_name = True
                await self.server_io.socket_output.write_message(
                    f'{client.client_name} send hi'
                )
                continue

            if request:
                await self.server_io.socket_output.write_message(
                    f'Message from {client.client_name} {request}'
                )
