from math import isqrt


def is_perfect_square(n: int) -> bool:
    """
    Return True if n is a perfect square, otherwise False.

    >>> is_perfect_square(16)
    True
    >>> is_perfect_square(15)
    False
    >>> is_perfect_square(0)
    True
    >>> is_perfect_square(1)
    True
    >>> is_perfect_square(-1)
    False
    >>> is_perfect_square(9)
    True
    >>> is_perfect_square(2)
    False
    """
    if n < 0:
        return False
    if n in (0, 1):
        return True
    root = isqrt(n)
    return root * root == n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
