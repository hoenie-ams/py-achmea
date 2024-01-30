"""
Demo functions
"""


def calculate_sales_tax(amount):
    """
    Return the calculated sales tax.

    Args:
    - amount (float): amount of money
    Returns:
        float: calculated tax
    """
    result = amount * 0.21
    return result


print(calculate_sales_tax(100))


def greet(name="stranger"):
    return "Hello " + name


print(greet("Eva"))
print(greet())


def menu(starter, main, dessert):
    print(f"Starter:    {starter}")
    print(f"Main:       {main}")
    print(f"Desser:     {dessert}")


menu(main="steak", starter="soup", dessert="icecream")


# Scope
x = 4


def foo():
    print(x)


foo()


def foo():
    y = 1
    print(y)


foo()
# print(y)  # error, out of scope!

z = 4


def foo():
    z = 100
    print("local z:", z)


foo()
print("global z:", z)
