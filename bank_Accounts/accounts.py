class Accounts:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.show_balance()

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance = self.balance - amount
            self.show_balance()
        else:
            print("The amount must be greater than 0 and no than your current balance")
            self.show_balance()

    def show_balance(self):
        print("The current balance is {}".format(self.balance))


user_1 = Accounts("John", 10000)
user_1.show_balance()
user_1.deposit(1200)
user_1.withdraw(630)

