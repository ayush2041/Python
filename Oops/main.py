class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")

    def check_balance(self):
        print(f"{self.name}'s Balance: {self.balance}")


user1 = BankAccount("Rahul", 1000)


user1.deposit(500)
user1.withdraw(300)
user1.check_balance()