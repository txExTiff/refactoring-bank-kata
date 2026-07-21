import datetime
from dataclasses import dataclass


class Clock:
    def get_date(self):
        return datetime.datetime.now()


@dataclass
class Transaction:
    date: datetime.datetime
    amount: int
    balance: int


class TransactionRepository:
    def __init__(self):
        self.transactions = []
        self.current_balance = 0

    def add_transaction(self, date, amount):
        self.transactions.append(
            Transaction(
                date=date,
                amount=amount,
                balance=self.current_balance + amount
            )
        )
        self.update_current_balance(amount)

    def update_current_balance(self, amount):
        self.current_balance = self.current_balance + amount

    def get_transactions(self):
        return self.transactions

    def get_sorted_from_recent_to_oldest(self):
        return sorted(self.transactions, key=lambda x: x.date, reverse=True)

    def get_length(self):
        return len(self.transactions)


class Printer:
    @staticmethod
    def print_formatted_transactions(transactions):
        print("Date       || Amount || Balance")
        for transaction in transactions:
            print(f'{transaction.date.strftime("%d/%m/%Y")} || {transaction.amount} || {transaction.balance}')


class Bank:
    def __init__(self, clock):
        self.transactionRepository = TransactionRepository()
        self.clock = clock

    def deposit(self, amount):
        self.make_new_transaction(amount)

    def withdraw(self, amount):
        self.make_new_transaction(-amount)

    def make_new_transaction(self, amount):
        self.transactionRepository.add_transaction(
            date=self.clock.get_date(),
            amount=amount
        )

    def print_statement(self):
        sorted_transactions = self.transactionRepository.get_sorted_from_recent_to_oldest()
        Printer.print_formatted_transactions(sorted_transactions)
