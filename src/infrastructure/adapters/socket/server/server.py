import socket

from src.domain.dto import Client
from src.domain.interfaces import BaseSocket
from src.domain.interfaces.base_repo import BaseClientsRepository

from src.domain.interfaces.server.base_command import BaseServerCommand
from src.infrastructure.adapters.io import BaseSocketIO


class BaseServer:
    def __init__(
            self,
            *,
            server: BaseSocket,
            socket_io: BaseSocketIO,
            client_repo: BaseClientsRepository,
            server_commander: BaseServerCommand

    ):
        self.server = server
        self.server_io = socket_io
        self.client_repo = client_repo
        self.server_commander = server_commander

    async def _accept(self):
        try:
            client_socket, client_address = self.server.socket.accept()
        except socket.timeout:
            return
        self.client_repo.append(
            Client(
                client_socket=client_socket,
                client_address=client_address
            ))
        self.client_repo.last.client_socket.settimeout(
            self.server.config.SOCKET_TIMEOUT
        )
        await self.server_io.socket_output.write_message(
            f"Client connected from {self.client_repo.last.client_address}"
        )
        self.client_repo.last.client_socket.send(
            self.server_commander.command_list.encode()
        )

    async def _close_all_connections(self):
        for client in self.client_repo:
            client.client_socket.close()
        self.server_io.delete_messages_file()

    async def _send_information_for_clients(self):
        if self.server_io.socket_input.value:
            for client in self.client_repo:
                client.client_socket.send(
                    self.server_io.socket_input.value.encode()
                )
            await self.server_io.socket_input.get_input()

    async def _get_information_for_clients(self):
        for client in self.client_repo:
            try:
                message = client.client_socket.recv(
                    self.server.config.RECV
                ).decode()
            except socket.timeout:
                continue

            if not client.client_name:
                await self.server_commander.client_without_name(
                    message,
                    client
                )
                continue

            if message:
                await self.server_commander.client_message(
                    client=client,
                    message=message
                )
