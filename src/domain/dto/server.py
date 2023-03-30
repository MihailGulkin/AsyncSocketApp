import dataclasses
import socket
from dataclasses import field

from src.domain.dto.base_socket import Address


@dataclasses.dataclass
class AcceptedClient:
    client_name: str
    client_socket: socket
    client_address: Address
    is_have_name: bool = field(default=False)
