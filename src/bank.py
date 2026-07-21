from src.clock import Clock
from src.transaction_repository import TransactionRepository
from src.printer import Printer


class Bank:
    def __init__(self, clock: Clock):
        self.transactionRepository = TransactionRepository()
        self.clock = clock

    def deposit(self, amount: int):
        self.make_new_transaction(amount)

    def withdraw(self, amount: int):
        self.make_new_transaction(-amount)

    def make_new_transaction(self, amount: int):
        self.transactionRepository.add_transaction(
            date=self.clock.get_date(),
            amount=amount
        )

    def print_statement(self):
        sorted_transactions = self.transactionRepository.get_sorted_from_recent_to_oldest()
        Printer.print_formatted_transactions(sorted_transactions)
