from src.adapters.io import SocketIO
from src.client.client_configurate import ClientSocketConfigurate
from src.client.client_io import ClientSocketIO
from src.domain.dto import Address
from src.settings import Config


class SocketClientRunner:
    @staticmethod
    async def run_server():
        client_name = input('Client name ---->')
        print(
            f"Client {client_name} is running"
        )
        client_config = ClientSocketConfigurate(
            address=Address(host=Config.SERVER_HOST, port=Config.SERVER_PORT),
            client_name=client_name
        )
        socket_io = SocketIO(
            file_name=fr'{Config.MESSAGES_DIR}\\{client_name}.txt'
        )
        client_socket_io = ClientSocketIO(
            client=client_config,
            socket_io=socket_io
        )

        await client_socket_io.client_io.socket_input.run_thread()

        while True:
            await client_socket_io.communication()
