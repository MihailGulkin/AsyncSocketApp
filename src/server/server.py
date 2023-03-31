from src.adapters.io import SocketIO
from src.domain.dto import (
    Address
)
from src.server.server_configurate import ServerSocketConfigurate
from src.server.server_io import ServerSocketIO
from src.settings import Config


class SocketServerRunner:
    @staticmethod
    async def run_server():
        print(
            f"Server is running on {Config.SERVER_HOST}:{Config.SERVER_PORT}"
        )
        server_config = ServerSocketConfigurate(
            address=Address(host=Config.SERVER_HOST, port=Config.SERVER_PORT)
        )
        socket_io = SocketIO(
            file_name=fr'{Config.MESSAGES_DIR}\\server.txt'
        )
        server_socket_io = ServerSocketIO(
            server=server_config,
            socket_io=socket_io
        )

        await server_socket_io.server_io.socket_input.run_thread()

        while True:
            await server_socket_io.communication()
