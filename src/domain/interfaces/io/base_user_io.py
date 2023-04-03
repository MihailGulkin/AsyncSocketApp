from abc import ABC, abstractmethod


class BaseUserInput(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.io_thread = None
        self.value = None

    @abstractmethod
    def _get_input(self) -> None:
        pass

    @abstractmethod
    async def get_input(self) -> None:
        pass
