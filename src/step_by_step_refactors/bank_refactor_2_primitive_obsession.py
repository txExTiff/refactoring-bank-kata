import datetime
from dataclasses import dataclass


class Clock:
    def __init__(self):
        # set current date
        self._date = datetime.datetime.now()

    def set_date(self, date):
        self._date = date

    def get_date(self, date):
        return self._date


@dataclass
class Transaction:
    date: datetime.datetime
    amount: int
    current_balance: int


class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def get_current_balance(self):
        return self.transactions[-1].current_balance

    def get_length(self):
        return len(self.transactions)


class Bank:
    def __init__(self, clock):
        # transactions tuple: date - amount - balance
        self.transactionRepository = TransactionRepository()
        self.clock = clock

    def deposit(self, amount):
        self.clock.set_date(datetime.datetime.now())
        previous_balance = 0
        # if list is empty you cannot get previous balance
        if self.transactionRepository.get_length() > 0:
            previous_balance = self.transactionRepository.get_current_balance()

        now = self.clock._date
        self.transactionRepository.add_transaction(
            Transaction(
                date=now,
                amount=amount,
                current_balance=previous_balance + amount
            )
        )

    def withdraw(self, amount):
        self.clock.set_date(datetime.datetime.now())
        previous_balance = 0
        # if list is empty you cannot get previous balance
        if self.transactionRepository.get_length() > 0:
            previous_balance = self.transactionRepository.get_current_balance()

        now = self.clock._date
        self.transactionRepository.add_transaction(
            Transaction(
                date=now,
                amount=-amount,
                current_balance=previous_balance - amount
            )
        )

    def print_statement(self):
        print("Date       || Amount || Balance")
        for transaction in self.transactionRepository.get_transactions()[::-1]:
            print(f'{transaction.date.strftime("%d/%m/%Y")} || {transaction.amount} || {transaction.current_balance}')

    def get_date(self):
        # not used
        return datetime.datetime.now()
