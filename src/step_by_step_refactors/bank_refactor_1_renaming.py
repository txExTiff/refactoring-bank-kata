import datetime


class Clock:
    def __init__(self):
        # set current date
        self._date = datetime.datetime.now()

    def set_date(self, date):
        self._date = date

    def get_date(self, date):
        return self._date


class Bank:
    def __init__(self, clock):
        # transactions tuple: date - amount - balance
        self.transactions = []
        self.clock = clock

    def deposit(self, amount):
        self.clock.set_date(datetime.datetime.now())
        previous_balance = 0
        # if list is empty you cannot get previous balance
        if len(self.transactions) > 0:
            previous_balance = self.transactions[-1][2]

        now = self.clock._date
        formatted_date = now.strftime("%d/%m/%Y")
        self.transactions.append([formatted_date, amount, previous_balance + amount])

    def withdraw(self, amount):
        self.clock.set_date(datetime.datetime.now())
        previous_balance = 0
        # if list is empty you cannot get previous balance
        if len(self.transactions) > 0:
            previous_balance = self.transactions[-1][2]

        now = self.clock._date
        formatted_date = now.strftime("%d/%m/%Y")
        self.transactions.append([formatted_date, -amount, previous_balance - amount])

    def print_statement(self):
        print("Date       || Amount || Balance")
        for transaction in self.transactions[::-1]:
            print(f"{transaction[0]} || {transaction[1]} || {transaction[2]}")

    def get_date(self):
        # not used
        return datetime.datetime.now()
