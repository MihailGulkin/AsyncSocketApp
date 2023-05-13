from abc import ABC, abstractmethod

from src.domain.consts.server_messages_command import LIST_OF_SERVER_COMMAND
from src.domain.dto import Client
from src.infrastructure.adapters.io import BaseSocketIO


class BaseServerCommand(ABC):
    def __init__(
            self,
            socket_io: BaseSocketIO
    ):
        self.socket_io = socket_io
        self.command_list = LIST_OF_SERVER_COMMAND

    @abstractmethod
    async def client_without_name(
            self,
            message: str,
            client: Client,
    ) -> None:
        pass

    @abstractmethod
    async def client_message(
            self,
            message: str,
            client: Client,
    ) -> None:
        pass
