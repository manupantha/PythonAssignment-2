class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to our online banking system")

    def deposit(self):
        amount = float(input("enter  amount for deposited:"))
        self.balance += amount
        print("\n amount deposited:", amount)

    def withdraw(self):
        amount = float(input("enter amount for withdrawn:"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n you withdraw:", amount)
        else:
            print("\n insufficient balance ")

    def display(self):
        print("\n Net balance=", self.balance)


asd = BankAccount()
asd.deposit()
asd.withdraw()
