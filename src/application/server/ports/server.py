from src.application.server.ports.server_io import ServerSocket
from src.domain.dto.config import BaseConfig

from src.application.server.ports.server_configurate import (
    ServerSocketConfigurate
)
from src.domain.interfaces.base_runner import BaseSocketRunner
from src.infrastructure.adapters.io.server import ServerSocketIO


class SocketServerRunner(BaseSocketRunner):
    @staticmethod
    async def run(config: BaseConfig) -> None:
        print(
            f"Server is running on "
            f"{config.Socket.SERVER_HOST}:{config.Socket.SERVER_PORT}"
        )

        server_socket_io = ServerSocket(
            server=ServerSocketConfigurate(
                config=config.Socket
            ),
            socket_io=ServerSocketIO(
                path_config=config.Paths,
                file_name='server.txt',
            )
        )

        await server_socket_io.server_io.socket_input.run_thread()

        while True:
            await server_socket_io.communication()
