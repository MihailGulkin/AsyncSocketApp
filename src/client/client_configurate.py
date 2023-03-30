import socket

from src.domain.dto import Address
from src.domain.interfaces import BaseSocket
from src.settings import Config


class ClientSocketConfigurate(BaseSocket):
    def __init__(
            self,
            address: Address,
            client_name: str
    ):
        self.client_name = client_name

        super().__init__(address)

    def _configurate_socket(self) -> socket:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(0.2)
        client_socket.connect((Config.SERVER_HOST, Config.SERVER_PORT))
        client_socket.send(self.client_name.encode())

        return client_socket
