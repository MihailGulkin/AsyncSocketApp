from src.infrastructure.adapters.socket.server.server import BaseServerSocket


class ServerSocket(BaseServerSocket):
    async def communication(self):
        if self.server_io.socket_input.value == 'exit':
            await self._close_all_connections()
            exit()
        await self._send_information_for_clients()
        await self._get_information_for_clients()
        await self._accept()
