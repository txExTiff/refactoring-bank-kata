# refactoring-bank-kata

A bank kata for practicing refactoring and code review, based on the [Codurance Bank Kata](https://www.codurance.com/katas/bank).

## What it does

Simulates a bank account that can deposit, withdraw, and print a statement with running balances:

```
Date       || Amount || Balance
14/01/2012 || -500   || 2500
13/01/2012 || 2000   || 3000
10/01/2012 || 1000   || 1000
```

## Project structure

```
src/
├── bank.py                  # Bank class — deposit, withdraw, print statement
├── clock.py                 # Clock — provides current date
├── transaction.py           # Transaction dataclass
├── transaction_repository.py # Stores and sorts transactions
├── printer.py               # Formats and prints statements
├── interest_calculator.py   # Calculates and applies interest
└── account.py               # Account with overdraft limit

tests/
├── test_bank_acceptance.py
├── test_clock.py
├── test_transaction.py
├── test_transaction_repository.py
├── test_printer.py
├── test_interest_calculator.py
└── test_account.py
```

## Running tests

```bash
python3 -m unittest discover -s tests -v
```

## Code smells and review opportunities

This codebase has intentional issues for practice:

- **Inconsistent naming** — `camelCase` (`interestRate`, `createdAt`) mixed with `snake_case` (`current_balance`, `overdraft_limit`)
- **Inconsistent error handling** — `Account` returns strings (`"insufficient funds"`), rest of codebase has no error handling at all
- **Bare except clause** — `InterestCalculator.apply_interest` silently swallows all exceptions
- **Incomplete features** — `Account.transfer_to` is stubbed with `pass`
- **Duplicated logic** — `Account.account_summary` formats output instead of reusing `Printer`
- **Missing validation** — no checks for negative deposits, negative interest rates
- **Bypassed constraints** — overdraft check in `Account.withdraw` is skipped if `Bank.withdraw` is called directly
- **Inconsistent type hints** — some files fully typed, others have no annotations
- **Untyped collection** — `InterestCalculator.history` is a bare `list` with dict entries instead of a typed structure
- **TODO comments** — compound interest and transfer features are unfinished
