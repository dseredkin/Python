"""
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.
The pass through the list is repeated until the list is sorted.

Time complexity: O(n^2)
"""

from __future__ import annotations


def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sorts the array using Bubble Sort algorithm.

    >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    >>> bubble_sort([5])
    [5]
    >>> bubble_sort([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> bubble_sort([4, 3, 2, 1])
    [1, 2, 3, 4]
    >>> bubble_sort([])
    []
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
