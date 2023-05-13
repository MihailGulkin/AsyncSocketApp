from src.domain.dto import Client
from src.domain.interfaces.base_repo import BaseClientsRepository


class ClientsRepository(BaseClientsRepository):
    def __init__(self):
        super().__init__()

    def __iter__(self) -> 'ClientsRepository':
        self.start = -1
        return self

    def __next__(self) -> Client:
        self.start += 1
        try:
            return self.clients[self.start]
        except IndexError:
            raise StopIteration

    def __len__(self) -> int:
        return len(self.clients)

    @property
    def last(self) -> Client:
        return self.clients[-1]

    def append(self, client: Client) -> None:
        self.clients.append(client)

    def remove(self, client: Client) -> None:
        self.clients.remove(client)

    def find_by_id(self, pk: int) -> Client | None:
        for client in self.clients:
            if client.client_id == pk:
                return client
        return None
