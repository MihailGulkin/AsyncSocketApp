from abc import ABC, abstractmethod

from src.domain.dto.config import BasePathsConfig
from src.infrastructure.adapters.io.base_io.user_input import UserInput
from src.infrastructure.adapters.io.base_io.write_message_to_file import (
    SocketWriteToFile
)


class SocketIO(ABC):
    def __init__(
            self,
            file_name: str,
            path_config: BasePathsConfig
    ):
        self.path_config = path_config

        self.socket_input = UserInput()
        self.socket_output = SocketWriteToFile(
            file_path=self.create_file_path(file_name)
        )

    @abstractmethod
    def create_file_path(self, file_name: str) -> str:
        """
        Create file path for server or client
        :return:
        """
        pass
