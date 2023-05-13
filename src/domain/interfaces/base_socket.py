from abc import abstractmethod, ABC
from socket import socket

from src.domain.dto import Address
from src.domain.dto.config import BaseSocketConfig


class BaseSocket(ABC):
    @abstractmethod
    def __init__(self, config: BaseSocketConfig):
        self.config = config
        self.address = Address(
            host=config.SERVER_HOST,
            port=config.SERVER_PORT
        )
        self.socket = self._configurate_socket()

    @abstractmethod
    def _configurate_socket(self) -> socket:
        pass
