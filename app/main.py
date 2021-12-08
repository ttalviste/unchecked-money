import datetime

from app.src.datastore.in_memory_eventstore import InMemoryEventStore
from app.src.expenses.add_expense import handle as expense_handler, AddExpense
from app.src.expenses.add_income import handle as income_handler, AddIncome


def run() -> None:
    datastore = InMemoryEventStore()
    income_handler(AddIncome(category='Wage', currency='EUR', amount=200, date=datetime.date.today()), datastore)
    income_handler(AddIncome(category='Loan', currency='EUR', amount=100, date=datetime.date.today()), datastore)
    expense_handler(AddExpense(category='Rent', amount=400, currency='EUR', date=datetime.date.today()), datastore)
    print(datastore.state())


if __name__ == '__main__':
    run()
