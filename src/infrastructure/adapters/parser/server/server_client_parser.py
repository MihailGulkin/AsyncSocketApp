from src.domain.dto.messages.command import MessageCommand
from src.domain.dto.messages.message import MessageCommandParser


class ClientMessageParser:
    def __init__(self, message: str):
        self.message = message

    def get_message_command(self) -> MessageCommand | None:
        if self.message == 'list':
            return MessageCommand.LIST_OF_USER
        if self.message == 'exit':
            return MessageCommand.EXIT
        message_ = self.message.split(' - ')
        try:
            if message_[0] == 'message':
                return MessageCommand.MESSAGE_TO_USER
        except IndexError:
            return MessageCommand.TEXT_TO_SERVER
        return MessageCommand.TEXT_TO_SERVER

    def pars_command(self) -> MessageCommandParser:
        _, id_, content = self.message.split(' - ')
        return MessageCommandParser(
            to_user=int(id_),
            content=content
        )
