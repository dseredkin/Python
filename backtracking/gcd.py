from __future__ import annotations


def gcd_euclidean(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    The Euclidean algorithm works by repeatedly applying the division lemma:
    GCD(a, b) = GCD(b, a % b) until b becomes 0, at which point GCD is a.

    Args:
        a: A non-negative integer.
        b: A non-negative integer.

    Returns:
        The GCD of a and b.

    Raises:
        ValueError: If either a or b is negative.

    >>> gcd_euclidean(48, 18)
    6
    >>> gcd_euclidean(10, 5)
    5
    >>> gcd_euclidean(7, 1)
    1
    >>> gcd_euclidean(0, 5)
    5
    >>> gcd_euclidean(5, 0)
    5
    >>> gcd_euclidean(-10, 5)
    Traceback (most recent call last):
        ...
    ValueError: Inputs must be non-negative integers
    >>> gcd_euclidean(10, -5)
    Traceback (most recent call last):
        ...
    ValueError: Inputs must be non-negative integers
    >>> gcd_euclidean(3.5, 2)
    Traceback (most recent call last):
        ...
    ValueError: Inputs must be integers
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")

    if b == 0:
        return a
    return gcd_euclidean(b, a % b)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
