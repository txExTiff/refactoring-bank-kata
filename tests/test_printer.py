import datetime
import io
import sys
import unittest

from src.transaction import Transaction
from src.printer import Printer


class TestPrinter(unittest.TestCase):

    def setUp(self):
        self.capture_output = io.StringIO()
        sys.stdout = self.capture_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_prints_header(self):
        Printer.print_formatted_transactions([])
        self.assertEqual(self.capture_output.getvalue(), "Date       || Amount || Balance\n")

    def test_prints_single_transaction(self):
        transactions = [
            Transaction(date=datetime.datetime(2023, 1, 10), amount=1000, balance=1000)
        ]
        Printer.print_formatted_transactions(transactions)
        expected = "Date       || Amount || Balance\n10/01/2023 || 1000 || 1000\n"
        self.assertEqual(self.capture_output.getvalue(), expected)

    def test_prints_multiple_transactions(self):
        transactions = [
            Transaction(date=datetime.datetime(2023, 1, 14), amount=-500, balance=2500),
            Transaction(date=datetime.datetime(2023, 1, 13), amount=2000, balance=3000),
            Transaction(date=datetime.datetime(2023, 1, 10), amount=1000, balance=1000),
        ]
        Printer.print_formatted_transactions(transactions)
        expected = (
            "Date       || Amount || Balance\n"
            "14/01/2023 || -500 || 2500\n"
            "13/01/2023 || 2000 || 3000\n"
            "10/01/2023 || 1000 || 1000\n"
        )
        self.assertEqual(self.capture_output.getvalue(), expected)

    def test_formats_date_as_dd_mm_yyyy(self):
        transactions = [
            Transaction(date=datetime.datetime(2023, 12, 5), amount=100, balance=100)
        ]
        Printer.print_formatted_transactions(transactions)
        self.assertIn("05/12/2023", self.capture_output.getvalue())
