import datetime
import unittest

from src.transaction import Transaction
from src.transaction_repository import TransactionRepository


class TestTransactionRepository(unittest.TestCase):

    def setUp(self):
        self.repo = TransactionRepository()

    def test_starts_empty(self):
        self.assertEqual(self.repo.get_length(), 0)
        self.assertEqual(self.repo.get_transactions(), [])

    def test_add_transaction_stores_transaction(self):
        date = datetime.datetime(2023, 1, 10)
        self.repo.add_transaction(date, 1000)
        self.assertEqual(self.repo.get_length(), 1)
        transaction = self.repo.get_transactions()[0]
        self.assertEqual(transaction, Transaction(date=date, amount=1000, balance=1000))

    def test_add_multiple_transactions_accumulates_balance(self):
        self.repo.add_transaction(datetime.datetime(2023, 1, 10), 1000)
        self.repo.add_transaction(datetime.datetime(2023, 1, 13), 2000)
        transactions = self.repo.get_transactions()
        self.assertEqual(transactions[0].balance, 1000)
        self.assertEqual(transactions[1].balance, 3000)

    def test_add_negative_amount_decreases_balance(self):
        self.repo.add_transaction(datetime.datetime(2023, 1, 10), 1000)
        self.repo.add_transaction(datetime.datetime(2023, 1, 11), -500)
        transactions = self.repo.get_transactions()
        self.assertEqual(transactions[1].balance, 500)

    def test_update_current_balance(self):
        self.repo.update_current_balance(500)
        self.assertEqual(self.repo.current_balance, 500)
        self.repo.update_current_balance(-200)
        self.assertEqual(self.repo.current_balance, 300)

    def test_get_sorted_from_recent_to_oldest(self):
        self.repo.add_transaction(datetime.datetime(2023, 1, 10), 1000)
        self.repo.add_transaction(datetime.datetime(2023, 1, 13), 2000)
        self.repo.add_transaction(datetime.datetime(2023, 1, 11), 500)
        sorted_transactions = self.repo.get_sorted_from_recent_to_oldest()
        dates = [t.date for t in sorted_transactions]
        self.assertEqual(dates, [
            datetime.datetime(2023, 1, 13),
            datetime.datetime(2023, 1, 11),
            datetime.datetime(2023, 1, 10),
        ])

    def test_get_sorted_does_not_mutate_original(self):
        self.repo.add_transaction(datetime.datetime(2023, 1, 13), 2000)
        self.repo.add_transaction(datetime.datetime(2023, 1, 10), 1000)
        original_first_date = self.repo.get_transactions()[0].date
        self.repo.get_sorted_from_recent_to_oldest()
        self.assertEqual(self.repo.get_transactions()[0].date, original_first_date)

    def test_get_length(self):
        self.assertEqual(self.repo.get_length(), 0)
        self.repo.add_transaction(datetime.datetime(2023, 1, 10), 100)
        self.assertEqual(self.repo.get_length(), 1)
        self.repo.add_transaction(datetime.datetime(2023, 1, 11), 200)
        self.assertEqual(self.repo.get_length(), 2)
