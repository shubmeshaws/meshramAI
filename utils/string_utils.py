```python
"""
String utility functions.

This module provides a set of functions for common string operations.
"""

def is_empty_string(input_string: str) -> bool:
    """
    Checks if the input string is empty.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()


def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates the input string to the specified maximum length.

    Args:
        input_string (str): The string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string


def pad_string(input_string: str, min_length: int, pad_char: str = " ") -> str:
    """
    Pads the input string with the specified character to the minimum length.

    Args:
        input_string (str): The string to pad.
        min_length (int): The minimum length of the output string.
        pad_char (str, optional): The character to use for padding. Defaults to " ".

    Returns:
        str: The padded string.
    """
    if len(input_string) < min_length:
        return input_string + pad_char * (min_length - len(input_string))
    return input_string


def split_string(input_string: str, delimiter: str) -> list[str]:
    """
    Splits the input string into a list of substrings using the specified delimiter.

    Args:
        input_string (str): The string to split.
        delimiter (str): The delimiter to use for splitting.

    Returns:
        list[str]: The list of substrings.
    """
    return input_string.split(delimiter)


def join_strings(strings: list[str], delimiter: str) -> str:
    """
    Joins the list of strings into a single string using the specified delimiter.

    Args:
        strings (list[str]): The list of strings to join.
        delimiter (str): The delimiter to use for joining.

    Returns:
        str: The joined string.
    """
    return delimiter.join(strings)
```
