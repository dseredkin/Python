from math import sqrt


def is_prime(n: int) -> bool:
    """
    Check if a number is prime using trial division.

    This function determines whether the given integer n is a prime number.
    A prime number is a natural number greater than 1 that has no positive divisors
    other than 1 and itself.

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    >>> is_prime(0)
    False
    >>> is_prime(-5)
    False
    >>> is_prime(17)
    True
    >>> is_prime(100)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
