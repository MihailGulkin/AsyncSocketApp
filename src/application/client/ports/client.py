from src.application.client.ports.services import (
    ClientSocket,
    ClientSocketConfigurate
)

from src.domain.dto.config.config import BaseConfig
from src.domain.exceptions.client.client import ServerNotStarted
from src.domain.interfaces.base_runner import BaseSocketRunner

from src.infrastructure.adapters.io.client import ClientSocketIO


class SocketClientRunner(BaseSocketRunner):
    @staticmethod
    async def run(config: BaseConfig) -> None:
        client_name = input('Client name ---->')

        try:
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
        except ServerNotStarted as e:
            print(e)
            return
        print(
            f"Client {client_name} is running"
        )
        await client_socket_io.client_io.socket_input.get_input()

        while True:
            await client_socket_io.communication()
