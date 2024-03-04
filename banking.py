class Account:
    def __init__(self, idd, name, balance):
        if isinstance(idd, int) and idd > 0:
            self.idd = idd
        else:
            raise ValueError("ID must be integer.")
        if isinstance(name, str) and len(name) > 0:
            self.name = name
        else:
            raise ValueError("Invalid name")
        if isinstance(balance, float):
            self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        actions.log(f"{self.name} added ${amount} to the balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        actions.log(f"{self.name} took ${amount} from the balance: {self.balance}")


class Transaction:
    def __init__(self):
        self.transactions = []

    def log(self, details):
        self.transactions.append(details)

    def getactions(self):
        return self.transactions

actions = Transaction()

first = Account(875,"Anonymous", 0.0)
first.deposit(-100)
first.withdraw(-200)


print(actions.getactions())

