from __future__ import annotations


def factorial_iterative(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n using an iterative approach.

    >>> factorial_iterative(5)
    120
    >>> factorial_iterative(0)
    1
    >>> factorial_iterative(1)
    1
    >>> factorial_iterative(10)
    3628800
    >>> factorial_iterative(4)
    24
    >>> import math
    >>> all(factorial_iterative(i) == math.factorial(i) for i in range(0, 11))
    True
    >>> factorial_iterative(-1)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError: n must be non-negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    result: int = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
