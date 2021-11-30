import dataclasses

from app.src.core.messages.commands import DomainCommand
from app.src.core.messages.events import DomainEvent
from app.src.datastore.datastore import EventStore


@dataclasses.dataclass(frozen=True)
class AddExpense(DomainCommand):
    category: str
    amount: float
    currency: str


@dataclasses.dataclass(frozen=True)
class ExpenseAdded(DomainEvent):
    category: str
    amount: float
    currency: str
    id: str = 'bla'


def handle(add_expense: AddExpense, event_store: EventStore):
    print(repr(add_expense))
    expense_added = ExpenseAdded(amount=add_expense.amount, category=add_expense.category, currency=add_expense.currency)
    event_store.publish(expense_added)
    return expense_added
