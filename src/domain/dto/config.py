from pathlib import Path
from typing import Protocol


class BasePathsConfig(Protocol):
    BASE_DIR: Path
    MESSAGES_DIR: Path


class BaseSocketConfig(Protocol):
    SOCKET_TIMEOUT: float
    SERVER_HOST: str
    SERVER_PORT: int


class BaseConfig(Protocol):
    Paths: BasePathsConfig
    Socket: BaseSocketConfig
