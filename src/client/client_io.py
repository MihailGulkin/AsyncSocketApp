import socket

from src.adapters.io import SocketIO
from src.domain.interfaces import BaseSocket


class ClientSocketIO:
    def __init__(
            self,
            client: BaseSocket,
            socket_io: SocketIO
    ):
        self.client = client
        self.client_io = socket_io

    async def _close_all_connection(self):
        self.client.socket.close()

    async def communication(self):
        if self.client_io.socket_input.value == 'exit':
            await self._close_all_connection()
            exit()
        await self._send_information_for_server()
        await self._get_information_for_server()

    async def _send_information_for_server(self):
        if self.client_io.socket_input.value:
            self.client.socket.send(self.client_io.socket_input.value.encode())
            await self.client_io.socket_input.run_thread()

    async def _get_information_for_server(self):
        try:
            request = self.client.socket.recv(1024).decode()
        except socket.timeout:
            return
        if request:
            await self.client_io.socket_output.write_message(
                f'Message from server {request}'
            )
