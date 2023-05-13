import socket

from src.domain.dto.config import BaseSocketConfig
from src.domain.exceptions.client.client import ServerNotStarted
from src.domain.interfaces import BaseSocket


class ClientSocketConfigurate(BaseSocket):
    def __init__(
            self,
            config: BaseSocketConfig,
            client_name: str
    ):
        self.client_name = client_name

        super().__init__(config=config)

    def _configurate_socket(self) -> socket:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(self.config.SOCKET_TIMEOUT)
        try:
            client_socket.connect((
                self.config.SERVER_HOST, self.config.SERVER_PORT
            ))
        except socket.timeout:
            raise ServerNotStarted('Server not started')
        client_socket.send(self.client_name.encode())

        return client_socket
