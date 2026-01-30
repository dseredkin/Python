from __future__ import annotations


def reverse_string(s: str) -> str:
    """
    Reverse the given string.

    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("")
    ''
    >>> reverse_string("a")
    'a'
    >>> reverse_string("Python")
    'nohtyP'
    """
    return s[::-1]
