import pytest

from app.src.datastore.in_memory_eventstore import InMemoryEventStore
from app.src.expenses.add_expenses import ExpenseAdded


def test_publish():
    datastore = InMemoryEventStore()
    expense_added = ExpenseAdded(currency='EUR', category='Rent', amount=420.00)
    datastore.publish(expense_added)


def test_publish_accepts_only_events():
    datastore = InMemoryEventStore()
    with pytest.raises(AssertionError):
        datastore.publish([])


def test_state():
    datastore = InMemoryEventStore()
    expense_added = ExpenseAdded(currency='EUR', category='Rent', amount=420.00)
    datastore.publish(expense_added)

    assert datastore.state() == 1
