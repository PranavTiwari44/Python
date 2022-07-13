import datetime
import pytz


class Accounts:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = []
        self._transaction_list.append((Accounts._current_time(), balance))
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
            self.show_balance()
            self._transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if self._balance >= amount > 0:
            self._balance = self._balance - amount
            self.show_balance()
            self._transaction_list.append((Accounts._current_time(), -amount))

        else:
            print("The amount must be greater than 0 and no than your current _balance")
            self.show_balance()

    def show_balance(self):
        print("The current balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


user_1 = Accounts("John", 10000)
user_1.show_balance()
user_1.deposit(1200)
user_1.withdraw(630)
user_1.show_transactions()
