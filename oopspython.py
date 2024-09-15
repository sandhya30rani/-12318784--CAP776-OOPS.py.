from abc import ABC, abstractmethod


class BankAccount(ABC):  
    def _init_(self, account_number, account_holder, balance=0):
        self._account_number = account_number  
        self._account_holder = account_holder  
        self._balance = balance  

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} deposited. New balance: {self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{amount} withdrawn. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def check_balance(self):
        print(f"Account holder: {self._account_holder}, Balance: {self._balance}")
    def get_account_number(self):
        return self._account_number

    def set_balance(self, new_balance):
        self._balance = new_balance


class SavingsAccount(BankAccount):
    def _init_(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super()._init_(account_number, account_holder, balance) 
        self.interest_rate = interest_rate
    
    
    def account_type(self):
        return "Savings Account"

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate
        print(f"Interest applied. New balance: {self._balance}")

class CurrentAccount(BankAccount):
    def _init_(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super()._init_(account_number, account_holder, balance) 
        self.overdraft_limit = overdraft_limit  

    
    def account_type(self):
        return "Current Account"

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"{amount} withdrawn. New balance: {self._balance}")
        else:
            print("Exceeded overdraft limit or invalid withdrawal amount.")


savings = SavingsAccount("1001", "sandy", 1000)
current = CurrentAccount("1002", "anil", 500)


print(f"sandy account type: {savings.account_type()}")
print(f"anil account type: {current.account_type()}")


savings.deposit(500)
savings.apply_interest()  

current.deposit(300)
current.withdraw(1000) 
savings.check_balance()
current.check_balance()
