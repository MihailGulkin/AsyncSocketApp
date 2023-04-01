from src.domain.dto.config import BasePathsConfig
from src.infrastructure.adapters.io import SocketIO


class ServerSocketIO(SocketIO):
    def __init__(self, file_name: str, path_config: BasePathsConfig):
        super().__init__(file_name, path_config)

    def create_file_path(self, file_name: str) -> str:
        return fr'{self.path_config.MESSAGES_DIR}\\server.txt'
