import datetime

from src.bank import Bank
from src.clock import Clock


class Account:
    def __init__(self, holder_name, clock, overdraft_limit=0):
        self.holder_name = holder_name
        self.bank = Bank(clock)
        self.overdraft_limit = overdraft_limit
        self.createdAt = datetime.datetime.now()
        self.is_active = True

    def deposit(self, amount) -> str:
        if not self.is_active:
            return "account closed"
        self.bank.deposit(amount)
        return "ok"

    def withdraw(self, amount) -> str:
        if not self.is_active:
            return "account closed"
        current = self.bank.transactionRepository.current_balance
        if current - amount < -self.overdraft_limit:
            return "insufficient funds"
        self.bank.withdraw(amount)
        return "ok"

    def get_balance(self):
        return self.bank.transactionRepository.current_balance

    def close_account(self):
        self.is_active = False

    def reopen_account(self):
        # TODO: should we check if balance is zero before reopening?
        self.is_active = True

    def account_summary(self) -> str:
        balance = self.get_balance()
        transactions = self.bank.transactionRepository.get_transactions()
        lines = []
        lines.append(f"Account: {self.holder_name}")
        lines.append(f"Balance: {balance}")
        lines.append(f"Transactions: {len(transactions)}")
        lines.append(f"Overdraft limit: {self.overdraft_limit}")
        lines.append(f"Status: {'active' if self.is_active else 'closed'}")
        return "\n".join(lines)

    def transfer_to(self, other_account, amount):
        # TODO: implement transfers between accounts
        pass

    def print_statement(self):
        self.bank.print_statement()
