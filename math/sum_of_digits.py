from __future__ import annotations


def sum_of_digits(number: int) -> int:
    """
    Calculate the sum of digits in a given non-negative integer.

    >>> sum_of_digits(123)
    6
    >>> sum_of_digits(0)
    0
    >>> sum_of_digits(999)
    27
    >>> sum_of_digits(4567)
    22
    >>> sum_of_digits(-123)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ValueError: Number must be non-negative
    """
    if number < 0:
        raise ValueError("Number must be non-negative")
    return sum(int(digit) for digit in str(number))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
