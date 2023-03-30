import socket

from src.domain.dto import Address
from src.domain.interfaces import BaseSocket


class ServerSocketConfigurate(BaseSocket):
    def __init__(
            self,
            address: Address,
    ):
        super().__init__(address)

    def _configurate_socket(self) -> socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.settimeout(0.1)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.address.host, self.address.port))
        server_socket.listen(5)
        return server_socket
