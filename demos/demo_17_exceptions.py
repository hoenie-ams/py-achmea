
try:
    print(1 / 0)
except ZeroDivisionError:
    print("not possible to divide by zero")

try:
    number = int(input("Give me a number: "))
    print(100 / number)
except ValueError:
    print("not a valid number")
except ZeroDivisionError:
    print("cannot divide by zero")
except Exception as error:
    print("Unexpected error", type(error), error)
finally:
    print("finally")


class PPError(Exception):
    """Custom exception for PP"""


def func(x):
    if x == 1:
        raise PPError("PP is weer vervelend")


try:
    func(1)
except PPError as error:
    print("Unexpected error", type(error), error)