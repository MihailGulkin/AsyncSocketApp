from src.infrastructure.adapters.socket.client.client import BaseClient


class ClientSocket(BaseClient):

    async def communication(self):
        if self.client_io.socket_input.value == 'exit':
            await self._close_all_connection()
            exit()
        await self._send_information_on_server()
        await self._retrieve_information_from_server()
