import socket

from src.domain.dto.config import BaseSocketConfig
from src.domain.interfaces import BaseSocket
from src.settings import Config


class ServerSocketConfigurate(BaseSocket):
    def __init__(
            self,
            config: BaseSocketConfig,
    ):
        super().__init__(config=config)

    def _configurate_socket(self) -> socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.settimeout(Config.Socket.SOCKET_TIMEOUT)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.address.host, self.address.port))
        server_socket.listen(5)
        return server_socket
