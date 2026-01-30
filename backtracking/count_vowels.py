from __future__ import annotations


def count_vowels(s: str) -> int:
    """
    Counts the number of vowels (a, e, i, o, u, both lowercase and uppercase) in the given string.

    >>> count_vowels("hello")
    2  # e and o
    >>> count_vowels("AEIOU")
    5
    >>> count_vowels("bcdfg")
    0
    >>> count_vowels("")
    0
    >>> count_vowels("aEiOu")
    5
    >>> count_vowels("Python Programming")
    4  # o, i, o, a
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
