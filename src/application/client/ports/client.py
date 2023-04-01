from src.application.client.ports.client_configurate import (
    ClientSocketConfigurate
)
from src.application.client.ports.client_io import ClientSocket

from src.domain.dto.config import BaseConfig
from src.domain.interfaces.base_runner import BaseSocketRunner

from src.infrastructure.adapters.io.client import ClientSocketIO


class SocketClientRunner(BaseSocketRunner):
    @staticmethod
    async def run(config: BaseConfig) -> None:
        client_name = input('Client name ---->')
        print(
            f"Client {client_name} is running"
        )
        client_socket_io = ClientSocket(
            client=ClientSocketConfigurate(
                client_name=client_name,
                config=config.Socket
            ),
            socket_io=ClientSocketIO(
                path_config=config.Paths,
                file_name=f'{client_name}'
            )
        )

        await client_socket_io.client_io.socket_input.run_thread()

        while True:
            await client_socket_io.communication()
