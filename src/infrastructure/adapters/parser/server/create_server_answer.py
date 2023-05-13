from src.domain.dto import Client
from src.domain.dto.messages.message import ServerAnswer
from src.domain.interfaces.base_repo import BaseClientsRepository
from src.infrastructure.adapters.parser.server.server_client_parser import \
    ClientMessageParser


class CreateServerAnswer:
    def __init__(
            self,
            message: str,
            client: Client,
            client_repo: BaseClientsRepository
    ):
        self.message_parser = ClientMessageParser(
            message
        )
        self.client = client
        self.client_repo = client_repo

    def create_message_to_server(self) -> str:
        return f'Notification from id: {self.client.client_id};' \
               f'name: {self.client.client_name};' \
               f'message: {self.message_parser.message}.'

    def create_list_of_user(self) -> str:
        msg = ''
        for client_ in self.client_repo:
            if client_ != self.client:
                msg += f'id: {client_.client_id}; name: {client_.client_name}'
        return msg if msg else 'All users offline'

    def create_message_to_user(self) -> ServerAnswer | str:
        msg = self.message_parser.pars_command()
        if client := self.client_repo.find_by_id(msg.to_user):
            return ServerAnswer(
                receiver=client,
                message_receiver=f'User: {self.client.client_name} send you message: {msg.content}',
                sender_message=f'Message successfully send to user: {client.client_id} - {client.client_name}'
            )
        return 'User not found'
