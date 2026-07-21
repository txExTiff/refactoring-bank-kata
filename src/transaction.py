import datetime
from dataclasses import dataclass


@dataclass
class Transaction:
    date: datetime.datetime
    amount: int
    balance: int
