"""
Demo object oriented programming
"""


class MyClass:
    """A simple class"""
    i = 12345

    def foo(self):
        return "hello world"


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"{self.owner} has EUR {self.balance}")


account_john = BankAccount("John")
account_jane = BankAccount("Jane")


class CustomInteger(int):
    def __init__(self, number):
        self.number = number

    def verdubbel(self):
        return self.number * 2


class Vehicle:
    def drive(self):
        print("let's go!")

    def brake(self):
        print("stopping")


class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass


class Motorbike(Vehicle):
    pass


car = Car()


class FilterModule:
    def filter(self):
        return {
            "filter_1": "filter_function",
        }


# house_number   -> snake_case
# PostalCode     -> PascalCase
# postalCode     -> camelCase
# postal-code    -> kebab-case
