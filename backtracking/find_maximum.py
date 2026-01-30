from __future__ import annotations


def find_maximum(numbers: list[float]) -> float:
    """
    Finds the largest element in a list without using the built-in max function.

    >>> find_maximum([1, 3, 2, 5, 4])
    5.0
    >>> find_maximum([5])
    5.0
    >>> find_maximum([-1, -2, -3])
    -1.0
    >>> find_maximum([])
    Traceback (most recent call last):
        ...
    ValueError: List must not be empty
    """
    if not numbers:
        raise ValueError("List must not be empty")
    return recursive_find_max(numbers, 0)


def recursive_find_max(numbers: list[float], index: int) -> float:
    """
    Helper function to recursively find the maximum element.

    >>> recursive_find_max([1, 3, 2], 0)
    3.0
    """
    if index == len(numbers) - 1:
        return numbers[index]
    max_rest = recursive_find_max(numbers, index + 1)
    if numbers[index] > max_rest:
        return numbers[index]
    return max_rest


if __name__ == "__main__":
    import doctest

    doctest.testmod()
