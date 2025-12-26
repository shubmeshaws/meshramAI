```python
"""
Utility functions for string manipulation.
"""

def is_valid_string(input_string):
    """
    Checks if the input is a non-empty string.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the input is a non-empty string, False otherwise.
    """
    return isinstance(input_string, str) and len(input_string.strip()) > 0


def trim_string(input_string):
    """
    Trims leading and trailing whitespace from the input string.

    Args:
        input_string (str): The input string to trim.

    Returns:
        str: The trimmed input string.
    """
    return input_string.strip()


def split_string(input_string, delimiter):
    """
    Splits the input string into a list of substrings based on the delimiter.

    Args:
        input_string (str): The input string to split.
        delimiter (str): The delimiter to split the string by.

    Returns:
        list: A list of substrings.
    """
    return input_string.split(delimiter)


def remove_special_chars(input_string):
    """
    Removes special characters from the input string.

    Args:
        input_string (str): The input string to remove special characters from.

    Returns:
        str: The input string with special characters removed.
    """
    return ''.join(e for e in input_string if e.isalnum() or e.isspace())
```
