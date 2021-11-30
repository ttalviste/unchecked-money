import dataclasses


@dataclasses.dataclass(frozen=True)
class AddExpense:
    category: str
    amount: float
    currency: str


@dataclasses.dataclass(frozen=True)
class ExpenseAdded:
    category: str
    amount: float
    currency: str
    id: str = 'bla'


def handle(add_expense: AddExpense):
    print(repr(add_expense))

    return ExpenseAdded(amount=add_expense.amount, category=add_expense.category, currency=add_expense.currency)
