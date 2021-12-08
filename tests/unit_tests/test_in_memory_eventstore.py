import datetime
import uuid

import pytest

from app.src.core import utils
from app.src.datastore.in_memory_eventstore import InMemoryEventStore
from app.src.expenses.add_expense import ExpenseAdded


def test_publish():
    datastore = InMemoryEventStore()
    expense_added = ExpenseAdded(
        id=utils.generate_id(), currency='EUR', category='Rent', amount=420.00, date=datetime.date.today())
    datastore.publish(expense_added)


def test_publish_accepts_only_events():
    datastore = InMemoryEventStore()
    with pytest.raises(AssertionError):
        datastore.publish([])


def test_state():
    datastore = InMemoryEventStore()
    expense_added = ExpenseAdded(
        id=utils.generate_id(), currency='EUR', category='Rent', amount=420.00, date=datetime.date.today())
    datastore.publish(expense_added)

    assert datastore.state() == 1
