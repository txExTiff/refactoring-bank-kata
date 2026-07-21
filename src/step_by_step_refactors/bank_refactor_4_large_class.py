import datetime
from dataclasses import dataclass


class Clock:
    def get_date(self):
        return datetime.datetime.now()


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
        if self.get_length() > 0:
            return self.transactions[-1].current_balance
        return 0

    def get_length(self):
        return len(self.transactions)


class Printer:
    @staticmethod
    def print_formatted_transactions(transactions):
        print("Date       || Amount || Balance")
        for transaction in transactions:
            print(f'{transaction.date.strftime("%d/%m/%Y")} || {transaction.amount} || {transaction.current_balance}')


class Bank:
    def __init__(self, clock):
        self.transactionRepository = TransactionRepository()
        self.clock = clock

    def deposit(self, amount):
        self.make_new_transaction(amount)

    def withdraw(self, amount):
        self.make_new_transaction(-amount)

    def make_new_transaction(self, amount):
        previous_balance = self.transactionRepository.get_current_balance()

        now = self.clock.get_date()
        self.transactionRepository.add_transaction(
            Transaction(
                date=now,
                amount=amount,
                current_balance=previous_balance + amount
            )
        )

    def print_statement(self):
        sorted_transactions = self.transactionRepository.get_transactions()[::-1]
        Printer.print_formatted_transactions(sorted_transactions)
