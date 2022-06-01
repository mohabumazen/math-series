import pytest
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_one():
    actual = fibonacci(0)
    expected = 0

    assert actual == expected

def test_two():
    actual = fibonacci(1)
    expected = 1

    assert actual == expected

def test_three():
    actual = fibonacci(2)
    expected = 1

    assert actual == expected

def test_four():
    actual = fibonacci(3)
    expected = 2

    assert actual == expected

def test_five():
    actual = lucas(0)
    expected = 2

    assert actual == expected

def test_six():
    actual = lucas(1)
    expected = 1

    assert actual == expected

def test_seven():
    actual = lucas(2)
    expected = 3

    assert actual == expected

def test_eight():
    actual = lucas(3)
    expected = 4

    assert actual == expected

def test_nine():
    actual = sum_series(0)
    expected = 0

    assert actual == expected

def test_ten():
    actual = sum_series(9)
    expected = 34

    assert actual == expected

