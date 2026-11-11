# Question 2: Encapsulation and Access Modifiers

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
        else:
            self.__balance += amount
            print(amount, "Birr deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(amount, "Birr withdrawn successfully.")
    def get_balance(self):
        return self.__balance
account1 = BankAccount("Ahmed", 10000)

print("Account Holder:", account1.account_holder)
print("Initial Balance:", account1.get_balance(), "Birr")
print("----------------------------")

account1.deposit(2000)

account1.withdraw(3000)

account1.deposit(-500)

account1.withdraw(-100)

account1.withdraw(20000)
print("----------------------------")
print("Account Holder:", account1.account_holder)
print("Final Balance:", account1.get_balance(), "Birr")