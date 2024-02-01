import math


def addition(x, y):
    return x + y


def divide(x, y):
    return x / y


def round_up(x):
    rounded = int(x) + int((x > 0) and (x - int(x)) > 0)
    return rounded


def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
