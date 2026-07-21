import datetime

from src.transaction_repository import TransactionRepository


class InterestCalculator:
    def __init__(self, transactionRepository: TransactionRepository):
        self.transactionRepository = transactionRepository
        self.interestRate = 0.0
        self.history = []

    def set_interest_rate(self, rate):
        self.interestRate = rate

    def get_interest_rate(self):
        return self.interestRate

    def calculate_interest(self) -> int:
        balance = self.transactionRepository.current_balance
        interest = int(balance * self.interestRate)
        return interest

    def apply_interest(self, clock):
        # TODO: implement compound interest option
        try:
            interest = self.calculate_interest()
            self.transactionRepository.add_transaction(
                date=clock.get_date(),
                amount=interest
            )
            self.history.append({
                "date": clock.get_date(),
                "interest": interest,
                "rate": self.interestRate
            })
        except:
            self.history.append({"error": True})

    def get_history(self):
        return self.history

    def get_total_interest_paid(self):
        total = 0
        for entry in self.history:
            if "interest" in entry:
                total = total + entry["interest"]
        return total

    def reset(self):
        self.interestRate = 0.0
        self.history = []
        # NOTE: does not reset transactionRepository — interest
        # transactions already added will remain

    def has_been_applied(self):
        for entry in self.history:
            if "interest" in entry:
                return True
        return False
