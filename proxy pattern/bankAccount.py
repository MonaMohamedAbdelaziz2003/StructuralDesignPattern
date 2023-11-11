from abc import ABC, abstractmethod


class Bank(ABC):
    @abstractmethod
    def getBalance(self):
        pass


class BankAccount(Bank):
    def getBalance(self):
        print("bank account server")
        return 2000
