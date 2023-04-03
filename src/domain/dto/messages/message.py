import dataclasses

from src.domain.dto import Client


@dataclasses.dataclass
class MessageCommandParser:
    to_user: int
    content: str


@dataclasses.dataclass
class ServerAnswer:
    to_client: Client
    message: str
