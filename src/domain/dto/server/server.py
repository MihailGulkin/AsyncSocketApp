import dataclasses
import socket
from dataclasses import field
from itertools import count
from src.domain.dto.common.base_socket import Address

counter = count()


@dataclasses.dataclass
class Client:
    client_socket: socket
    client_address: Address
    client_name: str = field(default='')
    client_id: int = field(default_factory=lambda: next(counter))

    def __eq__(self, other: 'Client'):
        if self.client_id == other.client_id:
            return True
        return False
