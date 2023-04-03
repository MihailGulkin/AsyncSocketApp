import threading

from src.domain.interfaces.io import BaseUserInput


class UserInput(BaseUserInput):
    def __init__(self) -> None:
        super().__init__()

    def _get_input(self) -> None:
        data = input('----->')
        self.value = data

    async def get_input(self) -> None:
        self.value = None
        self.io_thread = threading.Thread(target=self._get_input)
        self.io_thread.start()
