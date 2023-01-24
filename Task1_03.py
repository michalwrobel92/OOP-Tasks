class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = cash = 0


    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount

    def withdraw_cash(self, amount):
        if amount > 0:
            if amount < self.cash:
                self.cash -= amount
                return amount
            else:
                withdrawal = self.cash
                cash = 0
                return withdrawal

    def print_info(self):
        print(self.number, self.cash)

a = BankAccount(34234324)
print(a.cash)
print(a.number)
a.deposit_cash(300)
print(a.cash)
print(a.withdraw_cash(299))
a.print_info()
