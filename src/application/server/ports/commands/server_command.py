from src.domain.dto import Client
from src.domain.dto.messages.command import MessageCommand
from src.domain.interfaces.base_repo import BaseClientsRepository
from src.domain.interfaces.server.base_command import BaseServerCommand
from src.infrastructure.adapters.io import BaseSocketIO
from src.infrastructure.adapters.parser.server.create_server_answer import \
    CreateServerAnswer


class ServerCommand(BaseServerCommand):
    def __init__(
            self,
            socket_io: BaseSocketIO,
            client_repo: BaseClientsRepository
    ):
        super().__init__(socket_io=socket_io)
        self.client_repo = client_repo

    async def client_without_name(
            self,
            message: str,
            client: Client,
    ) -> None:
        client.client_name = f'{message}'
        await self.socket_io.socket_output.write_message(
            f'{client.client_name} send hi'
        )

    async def client_message(
            self,
            message: str,
            client: Client,
    ) -> None:
        answer = CreateServerAnswer(
            client=client,
            client_repo=self.client_repo,
            message=message
        )
        match answer.message_parser.get_message_command():
            case MessageCommand.TEXT_TO_SERVER:
                await self.socket_io.socket_output.write_message(
                    answer.create_message_to_server()
                )
            case MessageCommand.LIST_OF_USER:
                client.client_socket.send(
                    answer.create_list_of_user().encode()
                )
            case MessageCommand.MESSAGE_TO_USER:
                answer_ = answer.create_message_to_user()
                if not isinstance(answer_, str):
                    answer_.receiver.client_socket.send(
                        answer_.message_receiver.encode()
                    )
                    client.client_socket.send(
                        answer_.sender_message.encode()
                    )
                    return
                client.client_socket.send(
                    answer_.encode()
                )
