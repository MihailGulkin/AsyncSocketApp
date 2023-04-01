import threading


class SocketWriteToFile:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def _write_message(self, message: str) -> None:
        with open(self.file_path, 'a+', encoding='utf-8') as file:
            file.write(f'{message}\n')

    async def write_message(self, message: str) -> None:
        message_thread = threading.Thread(target=self._write_message, args=(
            message,
        ))
        message_thread.start()
