import math

import pytest

from demos.demo_18_tests import addition, divide, round_up, hypotenuse


def test_addition():
    actual = addition(3, 4)
    expected = 7
    assert actual == expected


def test_divide():
    assert divide(3, 2) == 1.5


def test_divide_raises_in_case_zero():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)


def test_round_up():
    assert round_up(2.4) == 3


def test_hypotenuse_calculates_correctly_for_positive_numbers():
    assert hypotenuse(3, 4) == 5


def test_hypotenuse_calculates_correctly_for_zero():
    assert hypotenuse(0, 0) == 0


def test_hypotenuse_calculates_correctly_for_negative_numbers():
    assert hypotenuse(-3, -4) == 5


def test_hypotenuse_calculates_correctly_for_mixed_positive_and_negative_numbers():
    assert hypotenuse(-3, 4) == 5


def test_hypotenuse_calculates_correctly_for_large_numbers():
    assert hypotenuse(1e6, 1e6) == math.sqrt(2) * 1e6
