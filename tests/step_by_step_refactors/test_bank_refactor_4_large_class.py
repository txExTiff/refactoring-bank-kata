from src.step_by_step_refactors.bank_refactor_4_large_class import Bank
import io
import sys
from unittest.mock import Mock, MagicMock
import datetime


class TestBankAcceptanceRefactor4:

    def test_should_print_full_statement_refactored(self):
        clock = Mock()
        bank = Bank(clock)
        capture_output = io.StringIO()
        sys.stdout = capture_output

        clock.get_date.side_effect = [
            datetime.datetime(2012, 1, 10),
            datetime.datetime(2012, 1, 13),
            datetime.datetime(2012, 1, 14)
        ]

        bank.deposit(1000)
        bank.deposit(2000)
        bank.withdraw(500)
        bank.print_statement()

        expected_output = """Date       || Amount || Balance
14/01/2012 || -500 || 2500
13/01/2012 || 2000 || 3000
10/01/2012 || 1000 || 1000
"""

        sys.stdout = sys.__stdout__
        assert capture_output.getvalue() == expected_output
