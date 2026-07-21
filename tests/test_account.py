import datetime
import io
import sys
import unittest
from unittest.mock import Mock

from src.account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.clock = Mock()
        self.clock.get_date.return_value = datetime.datetime(2023, 1, 10)

    def test_deposit(self):
        account = Account("Alice", self.clock)
        result = account.deposit(1000)
        self.assertEqual(result, "ok")
        self.assertEqual(account.get_balance(), 1000)

    def test_withdraw(self):
        account = Account("Alice", self.clock)
        account.deposit(1000)
        result = account.withdraw(500)
        self.assertEqual(result, "ok")
        self.assertEqual(account.get_balance(), 500)

    def test_withdraw_insufficient_funds(self):
        account = Account("Alice", self.clock)
        account.deposit(100)
        result = account.withdraw(200)
        self.assertEqual(result, "insufficient funds")
        self.assertEqual(account.get_balance(), 100)

    def test_withdraw_with_overdraft_limit(self):
        account = Account("Alice", self.clock, overdraft_limit=500)
        account.deposit(100)
        result = account.withdraw(400)
        self.assertEqual(result, "ok")
        self.assertEqual(account.get_balance(), -300)

    def test_withdraw_exceeds_overdraft_limit(self):
        account = Account("Alice", self.clock, overdraft_limit=100)
        result = account.withdraw(200)
        self.assertEqual(result, "insufficient funds")

    def test_closed_account_rejects_deposit(self):
        account = Account("Alice", self.clock)
        account.close_account()
        result = account.deposit(1000)
        self.assertEqual(result, "account closed")

    def test_closed_account_rejects_withdraw(self):
        account = Account("Alice", self.clock)
        account.deposit(1000)
        account.close_account()
        result = account.withdraw(100)
        self.assertEqual(result, "account closed")

    def test_reopen_account(self):
        account = Account("Alice", self.clock)
        account.close_account()
        account.reopen_account()
        result = account.deposit(500)
        self.assertEqual(result, "ok")

    def test_account_summary(self):
        account = Account("Bob", self.clock, overdraft_limit=200)
        account.deposit(1000)
        summary = account.account_summary()
        self.assertIn("Account: Bob", summary)
        self.assertIn("Balance: 1000", summary)
        self.assertIn("Overdraft limit: 200", summary)
        self.assertIn("Status: active", summary)

    def test_transfer_to_is_not_implemented(self):
        a1 = Account("Alice", self.clock)
        a2 = Account("Bob", self.clock)
        a1.deposit(1000)
        result = a1.transfer_to(a2, 500)
        self.assertIsNone(result)
