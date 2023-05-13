from abc import ABC, abstractmethod

from src.domain.dto.config import BaseConfig


class BaseSocketRunner(ABC):
    @staticmethod
    @abstractmethod
    def run(config: BaseConfig) -> None:
        """
        Run client or server
        :return:
        """
        pass
