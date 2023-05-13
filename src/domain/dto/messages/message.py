import dataclasses

from src.domain.dto import Client


@dataclasses.dataclass
class MessageCommandParser:
    to_user: int
    content: str


@dataclasses.dataclass
class ServerAnswer:
    receiver: Client
    message_receiver: str
    sender_message: str
