import datetime

from src.transaction import Transaction


class TransactionRepository:
    def __init__(self):
        self.transactions: list[Transaction] = []
        self.current_balance: int = 0

    def add_transaction(self, date: datetime.datetime, amount: int):
        self.transactions.append(
            Transaction(
                date=date,
                amount=amount,
                balance=self.current_balance + amount
            )
        )
        self.update_current_balance(amount)

    def update_current_balance(self, amount: int):
        self.current_balance = self.current_balance + amount

    def get_transactions(self) -> list[Transaction]:
        return self.transactions

    def get_sorted_from_recent_to_oldest(self) -> list[Transaction]:
        return sorted(self.transactions, key=lambda x: x.date, reverse=True)

    def get_length(self) -> int:
        return len(self.transactions)
