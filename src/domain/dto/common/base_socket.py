import dataclasses


@dataclasses.dataclass
class Address:
    host: str
    port: int


