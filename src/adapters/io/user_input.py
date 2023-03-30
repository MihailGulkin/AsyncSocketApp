import threading


class UserInput:
    def __init__(self) -> None:
        self.io_thread = None
        self.value = None

    def get_input(self) -> None:
        data = input('----->')
        self.value = data

    async def run_thread(self) -> None:
        self.value = None
        self.io_thread = threading.Thread(target=self.get_input)
        self.io_thread.start()
