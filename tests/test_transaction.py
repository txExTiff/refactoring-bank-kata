import datetime
import unittest

from src.transaction import Transaction


class TestTransaction(unittest.TestCase):

    def test_stores_date_amount_and_balance(self):
        date = datetime.datetime(2023, 5, 1)
        transaction = Transaction(date=date, amount=500, balance=500)
        self.assertEqual(transaction.date, date)
        self.assertEqual(transaction.amount, 500)
        self.assertEqual(transaction.balance, 500)

    def test_equality_by_value(self):
        date = datetime.datetime(2023, 5, 1)
        t1 = Transaction(date=date, amount=100, balance=100)
        t2 = Transaction(date=date, amount=100, balance=100)
        self.assertEqual(t1, t2)

    def test_inequality_when_values_differ(self):
        date = datetime.datetime(2023, 5, 1)
        t1 = Transaction(date=date, amount=100, balance=100)
        t2 = Transaction(date=date, amount=200, balance=200)
        self.assertNotEqual(t1, t2)
