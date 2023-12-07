class Expense:
    def __init__(self, amount):
        self.amount = amount


class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, expense):
        if self.successor:
            self.successor.handle_request(expense)


class ManagerHandler(Handler):
    def handle_request(self, expense):
        if expense.amount <= 100:
            print(f"Manager approves expense of ${expense.amount}")
        else:
            super().handle_request(expense)


class DirectorHandler(Handler):
    def handle_request(self, expense):
        if 100 < expense.amount <= 500:
            print(f"Director approves expense of ${expense.amount}")
        else:
            super().handle_request(expense)


class CFOHandler(Handler):
    def handle_request(self, expense):
        if 500 < expense.amount <= 1000:
            print(f"CFO approves expense of ${expense.amount}")
        else:
            super().handle_request(expense)


class PresidentHandler(Handler):
    def handle_request(self, expense):
        if expense.amount > 1000:
            print(f"President approves expense of ${expense.amount}")
        else:
            super().handle_request(expense)


def main():
    # Creating the chain of responsibility
    president_handler = PresidentHandler()
    cfo_handler = CFOHandler(president_handler)
    director_handler = DirectorHandler(cfo_handler)
    manager_handler = ManagerHandler(director_handler)

    # Example expenses
    expenses = [Expense(50), Expense(200), Expense(700), Expense(1500)]

    # Processing expenses
    for expense in expenses:
        print(f"Processing expense of ${expense.amount}:")
        manager_handler.handle_request(expense)
        print("-" * 30)


if __name__ == "__main__":
    main()
