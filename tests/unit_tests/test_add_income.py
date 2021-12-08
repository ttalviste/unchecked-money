import datetime

from pytest_mock import MockerFixture

import app
from app.src.core import utils
from app.src.datastore.in_memory_eventstore import InMemoryEventStore
from app.src.expenses import add_income
from app.src.expenses.add_income import AddIncome, IncomeAdded


def test_handle(mocker: MockerFixture) -> None:
    mocker.patch(
        'app.src.core.utils.uuid.uuid4',
        return_value='random_uuid'
    )
    event_store = InMemoryEventStore()
    add_income_handler = add_income.handle
    add_test_income = AddIncome(
        category='Wage',
        amount=2000.00,
        currency='EUR',
        date=datetime.date.today()
    )
    income_added = IncomeAdded(
        id=utils.generate_id(),
        category=add_test_income.category,
        amount=add_test_income.amount,
        currency=add_test_income.currency,
        date=add_test_income.date

    )

    assert add_income_handler(add_test_income, event_store) == income_added
    assert event_store.state() == [income_added]
