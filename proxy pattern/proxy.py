from bankAccount import BankAccount

class BankAccountProxy(BankAccount):
    def __init__(self):
        self.BankAccount=BankAccount

    def getBalance(self):
        balance=self.BankAccount.getBalance(self)
        return balance
