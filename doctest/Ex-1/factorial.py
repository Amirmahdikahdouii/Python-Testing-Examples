"""
Module Level DocString:

In This module, we have a function called factorial that calculate factorial for us.

>>> factorial(5)
120

>>> factorial(6)
720
"""


def factorial(number):
    """
    Factorial Function:
    Calculate factorial by recursive mode function.

    >>> factorial(0)
    1

    >>> factorial(2.5)
    Traceback (most recent call last):
    ...
    ValueError: Number Should be Non-negative integers

    >>> factorial(-5)
    Traceback (most recent call last):
    ...
    ValueError: Number Should be Non-negative integers


    >>> factorial(None)
    Traceback (most recent call last):
    ...
    ValueError: Number Should be Non-negative integers

    >>> factorial(501)
    Traceback (most recent call last):
    ...
    ValueError: Number is too much!
    """

    if not isinstance(number, int) or number < 0:
        raise ValueError("Number Should be Non-negative integers")
    elif number > 500:
        raise ValueError("Number is too much!")
    return number * factorial(number-1) if number > 1 else 1
