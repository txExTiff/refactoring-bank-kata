from src.transaction import Transaction


class Printer:
    @staticmethod
    def print_formatted_transactions(transactions: list[Transaction]):
        print("Date       || Amount || Balance")
        for transaction in transactions:
            print(f'{transaction.date.strftime("%d/%m/%Y")} || {transaction.amount} || {transaction.balance}')
