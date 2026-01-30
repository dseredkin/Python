def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome, ignoring case and spaces.

    >>> is_palindrome("A man a plan a canal Panama")
    True
    >>> is_palindrome("race a car")
    False
    >>> is_palindrome("")
    True  # An empty string is considered a palindrome
    >>> is_palindrome("a")
    True
    >>> is_palindrome("Ab Ba")
    True
    >>> is_palindrome("Hello World")
    False
    """
    # Remove spaces and convert to lowercase
    cleaned = "".join(c.lower() for c in s if c != " ")
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
