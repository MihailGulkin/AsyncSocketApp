from src.domain.interfaces import BaseSocket

from src.domain.interfaces.base_repo import BaseClientsRepository
from src.domain.interfaces.server.base_command import BaseServerCommand
from src.infrastructure.adapters.io import BaseSocketIO

from src.infrastructure.adapters.socket.server import BaseServer


class ServerSocket(BaseServer):
    def __init__(
            self,
            *,
            server: BaseSocket,
            socket_io: BaseSocketIO,
            repo: BaseClientsRepository,
            server_commander: BaseServerCommand
    ):
        super().__init__(
            server=server,
            socket_io=socket_io,
            client_repo=repo,
            server_commander=server_commander
        )

    async def communication(self):
        if self.server_io.socket_input.value == 'exit':
            await self._close_all_connections()
            exit()
        await self._send_information_for_clients()
        await self._get_information_for_clients()
        await self._accept()
