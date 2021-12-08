import dataclasses
import datetime

from app.src.core import utils
from app.src.core.messages.commands import DomainCommand
from app.src.core.messages.events import DomainEvent, EXPENSE_ADDED
from app.src.datastore.datastore import EventStore


@dataclasses.dataclass(frozen=True)
class AddExpense(DomainCommand):
    category: str
    amount: float
    currency: str
    date: datetime.date


@dataclasses.dataclass(frozen=True)
class ExpenseAdded(DomainEvent):
    category: str
    amount: float
    currency: str
    date: datetime.date

    def get_type(self) -> str:
        return EXPENSE_ADDED


def handle(add_expense: AddExpense, event_store: EventStore):
    print(repr(add_expense))
    expense_added = ExpenseAdded(
        id=utils.generate_id(),
        amount=add_expense.amount,
        category=add_expense.category,
        currency=add_expense.currency,
        date=add_expense.date
    )
    event_store.publish(expense_added)
    return expense_added
