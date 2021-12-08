import dataclasses
from abc import ABC

EXPENSE_ADDED = 'EXPENSE_ADDED'
EXPENSE_REMOVED = 'EXPENSE_REMOVED'
INCOME_ADDED = 'INCOME_ADDED'
INCOME_REMOVED = 'INCOME_REMOVED'


@dataclasses.dataclass(frozen=True)
class DomainEvent(ABC):
    id: str

    def get_type(self) -> str:
        ...
