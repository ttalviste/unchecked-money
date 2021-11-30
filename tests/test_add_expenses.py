from app.src.datastore.in_memory_eventstore import InMemoryEventStore
from app.src.expenses import add_expenses
from app.src.expenses.add_expenses import AddExpense, ExpenseAdded


def test_handle():
    event_store = InMemoryEventStore()
    add_expense_handler = add_expenses.handle
    add_test_expense = AddExpense(category='Rent', amount=420.00, currency='EUR')
    expense_added = ExpenseAdded(
        category=add_test_expense.category,
        amount=add_test_expense.amount,
        currency=add_test_expense.currency
    )
    assert add_expense_handler(add_test_expense, event_store) == expense_added
    assert event_store.state() == 1
