import dataclasses
from abc import ABC


@dataclasses.dataclass(frozen=True)
class DomainEvent(ABC):
    ...
