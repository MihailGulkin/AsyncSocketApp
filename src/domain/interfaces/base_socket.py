from abc import abstractmethod, ABC
from socket import socket

from src.domain.dto import Address


class BaseSocket(ABC):
    @abstractmethod
    def __init__(self, address: Address):
        self.address = address
        self.socket = self._configurate_socket()

    @abstractmethod
    def _configurate_socket(self) -> socket:
        pass
