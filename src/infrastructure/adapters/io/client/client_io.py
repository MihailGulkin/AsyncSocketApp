import os.path

from src.domain.dto.config import BasePathsConfig
from src.infrastructure.adapters.io import BaseSocketIO
from src.infrastructure.adapters.io.utils.generate_random_value import \
    generate_string


class ClientSocketIO(BaseSocketIO):
    def __init__(self, file_name: str, path_config: BasePathsConfig):
        super().__init__(file_name, path_config)

    def create_file_path(self, file_name: str) -> str:
        return os.path.join(
            self.path_config.MESSAGES_DIR,
            f'client_{file_name}_{generate_string()}.txt'
        )
