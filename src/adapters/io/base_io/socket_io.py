from src.adapters.io.base_io.user_input import UserInput
from src.adapters.io.base_io.write_message_to_file import SocketWriteToFile


class SocketIO:
    def __init__(self, file_name: str):
        self.socket_input = UserInput()
        self.socket_output = SocketWriteToFile(
            file_name=file_name
        )
