from abc import ABC, abstractmethod


class BaseSocketWriteToFile(ABC):
    @abstractmethod
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    @abstractmethod
    def _write_message(self, message: str) -> None:
        """
        Function for write in file
        :param message:
        :return:
        """
        pass

    @abstractmethod
    async def write_message(self, message: str) -> None:
        """
        Create and run io thread.
        :param message:
        :return:
        """
        pass
