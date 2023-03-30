import socket

from src.adapters.io import SocketIO
from src.domain.dto import AcceptedClient
from src.server.server_configurate import ServerSocketConfigurate


class ServerSocketIO:
    def __init__(
            self,
            server: ServerSocketConfigurate,
            socket_io: SocketIO
    ):
        self.server = server
        self.server_io = socket_io
        self.clients: list[AcceptedClient] = []

    async def accept(self):
        try:
            client_socket, client_address = self.server.socket.accept()
            self.clients.append(
                AcceptedClient(
                    client_name=f'client_{len(self.clients)}',
                    client_socket=client_socket,
                    client_address=client_address
                ))
            await self.server_io.socket_output.write_message(
                f"Client connected from {self.clients[-1].client_address}"
            )
        except socket.timeout:
            pass

    async def _close_all_connection(self):
        for client in self.clients:
            client.client_socket.close()

    async def communication(self):
        if self.server_io.socket_input.value == 'exit':
            await self._close_all_connection()
            exit()
        print('Before send info')
        await self.send_information_for_clients()
        print('After send inf')
        await self.get_information_for_clients()
        print('After get info and send info')

    async def send_information_for_clients(self):
        if self.server_io.socket_input.value:
            for client in self.clients:
                client.client_socket.send(
                    self.server_io.socket_input.value.encode()
                )
            await self.server_io.socket_input.run_thread()

    async def get_information_for_clients(self):
        for client in self.clients:
            request = client.client_socket.recv(1024).decode()
            if not client.is_have_name:
                client.client_name = f'{client.client_name} - {request}'
                await self.server_io.socket_output.write_message(
                    f'{client.client_name} send hi'
                )
                return

            if request:
                await self.server_io.socket_output.write_message(
                    f'Message from {client.client_name} {request}'
                )
