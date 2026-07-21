import datetime
import unittest
from unittest.mock import Mock

from src.transaction_repository import TransactionRepository
from src.interest_calculator import InterestCalculator


class TestInterestCalculator(unittest.TestCase):

    def setUp(self):
        self.repo = TransactionRepository()
        self.calculator = InterestCalculator(self.repo)
        self.clock = Mock()
        self.clock.get_date.return_value = datetime.datetime(2023, 6, 1)

    def test_default_interest_rate_is_zero(self):
        self.assertEqual(self.calculator.get_interest_rate(), 0.0)

    def test_set_interest_rate(self):
        self.calculator.set_interest_rate(0.05)
        self.assertEqual(self.calculator.get_interest_rate(), 0.05)

    def test_calculate_interest_on_zero_balance(self):
        self.calculator.set_interest_rate(0.1)
        self.assertEqual(self.calculator.calculate_interest(), 0)

    def test_calculate_interest_on_positive_balance(self):
        self.repo.add_transaction(datetime.datetime(2023, 1, 1), 1000)
        self.calculator.set_interest_rate(0.1)
        self.assertEqual(self.calculator.calculate_interest(), 100)

    def test_apply_interest_adds_transaction(self):
        self.repo.add_transaction(datetime.datetime(2023, 1, 1), 1000)
        self.calculator.set_interest_rate(0.05)
        self.calculator.apply_interest(self.clock)
        self.assertEqual(self.repo.get_length(), 2)
        self.assertEqual(self.repo.current_balance, 1050)

    def test_apply_interest_records_history(self):
        self.repo.add_transaction(datetime.datetime(2023, 1, 1), 2000)
        self.calculator.set_interest_rate(0.1)
        self.calculator.apply_interest(self.clock)
        history = self.calculator.get_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["interest"], 200)

    def test_get_total_interest_paid(self):
        self.repo.add_transaction(datetime.datetime(2023, 1, 1), 1000)
        self.calculator.set_interest_rate(0.1)
        self.calculator.apply_interest(self.clock)
        self.calculator.apply_interest(self.clock)
        self.assertEqual(self.calculator.get_total_interest_paid(), 210)

    def test_history_starts_empty(self):
        self.assertEqual(self.calculator.get_history(), [])
