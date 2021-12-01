import datetime

from app.src.datastore.in_memory_eventstore import InMemoryEventStore
from app.src.expenses import add_income
from app.src.expenses.add_income import AddIncome, IncomeAdded


def test_handle():
    event_store = InMemoryEventStore()
    add_income_handler = add_income.handle
    add_test_income = AddIncome(category='Wage', amount=2000.00, currency='EUR', date=datetime.date.today())
    income_added = IncomeAdded(
        category=add_test_income.category,
        amount=add_test_income.amount,
        currency=add_test_income.currency,
        date=add_test_income.date

    )

    assert add_income_handler(add_test_income, event_store) == income_added
    assert event_store.state() == 1
