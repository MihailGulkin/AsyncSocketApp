from enum import Enum


class MessageCommand(Enum):
    LIST_OF_USER = 'list'
    MESSAGE_TO_USER = 'message'
    TEXT_TO_SERVER = 'server'
