from src.application.server.ports.commands.server_command import ServerCommand
from src.application.server.ports.services import (
    ServerSocketConfigurate,
    ServerSocket
)

from src.domain.dto.config import BaseConfig
from src.domain.interfaces.base_runner import BaseSocketRunner

from src.infrastructure.adapters.io.server import ServerSocketIO
from src.infrastructure.adapters.repositories.client_repo import (
    ClientsRepository
)


class SocketServerRunner(BaseSocketRunner):
    @staticmethod
    async def run(config: BaseConfig) -> None:
        print(
            f"Server is running on "
            f"{config.Socket.SERVER_HOST}:{config.Socket.SERVER_PORT}"
        )

        socket_io = ServerSocketIO(
            path_config=config.Paths,
            file_name='server.txt',
        )
        repo = ClientsRepository()

        server_socket_io = ServerSocket(
            server=ServerSocketConfigurate(
                config=config.Socket
            ),
            socket_io=socket_io,
            repo=repo,
            server_commander=ServerCommand(
                socket_io=socket_io,
                client_repo=repo

            )
        )

        await server_socket_io.server_io.socket_input.get_input()

        while True:
            await server_socket_io.communication()
