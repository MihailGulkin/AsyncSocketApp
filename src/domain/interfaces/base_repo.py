from abc import ABC, abstractmethod

from src.domain.dto import Client


class BaseClientsRepository(ABC):
    def __init__(self):
        self.clients: list[Client] = []

    @abstractmethod
    def __iter__(self) -> 'BaseClientsRepository':
        pass

    @abstractmethod
    def __next__(self) -> Client:
        pass

    def __len__(self) -> int:
        pass

    @property
    @abstractmethod
    def last(self) -> Client:
        pass

    @abstractmethod
    def append(self, client: Client) -> None:
        pass

    @abstractmethod
    def find_by_id(self, pk: int) -> Client | None:
        pass
