import datetime

from pytest_mock import MockerFixture

from app.src.core import utils
from app.src.datastore.in_memory_eventstore import InMemoryEventStore
from app.src.expenses import add_expense
from app.src.expenses.add_expense import AddExpense, ExpenseAdded


def test_handle(mocker: MockerFixture) -> None:
    mocker.patch(
        'app.src.core.utils.uuid.uuid4',
        return_value='random_uuid'
    )
    event_store = InMemoryEventStore()
    add_expense_handler = add_expense.handle
    add_test_expense = AddExpense(category='Rent', amount=420.00, currency='EUR', date=datetime.date.today())
    expense_added = ExpenseAdded(
        id=utils.generate_id(),
        category=add_test_expense.category,
        amount=add_test_expense.amount,
        currency=add_test_expense.currency,
        date=add_test_expense.date
    )
    assert add_expense_handler(add_test_expense, event_store) == expense_added
    assert event_store.state() == 1
