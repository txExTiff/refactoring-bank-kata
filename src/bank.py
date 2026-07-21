import datetime


class Clock:
    def __init__(self):
        # set current date
        self._d = datetime.datetime.now()

    def set_date(self, d):
        self._d = d
    def get_date(self, d):
        return self._d


class Bank:
    def __init__(self, clock):
        # transactions tuple: date - amount - balance
        self.transaction = []
        self.clock = clock

    def deposit(self, amount):
        self.clock.set_date(datetime.datetime.now())
        previous_balance = 0
        # if list is empty you cannot get previous balance
        if len(self.transaction) > 0:
            previous_balance = self.transaction[-1][2]

        t = self.clock._date
        new_d = t.strftime("%d/%m/%Y")
        self.transaction.append([new_d, amount, previous_balance + amount])

    def withdraw(self, amount):
        self.clock.set_date(datetime.datetime.now())
        b = 0
        # if list is empty you cannot get previous balance
        if len(self.transaction) > 0:
            b = self.transaction[-1][2]

        t = self.clock._date
        new_d = t.strftime("%d/%m/%Y")
        self.transaction.append([new_d, -amount, b - amount])

    def print_statement(self):
        print("Date       || Amount || Balance")
        for i in self.transaction[::-1]:
            print(f"{i[0]} || {i[1]} || {i[2]}")

    def get_date(self):
        # not used
        return datetime.datetime.now()
