```python
"""
Utility functions for string manipulation.
"""

def to_title_case(input_string: str) -> str:
    """
    Converts a string to title case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The input string in title case.
    """
    return input_string.title()


def is_empty_string(input_string: str) -> bool:
    """
    Checks if a string is empty.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return len(input_string.strip()) == 0


def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncates a string to a specified maximum length.

    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated input string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string


def remove_special_characters(input_string: str) -> str:
    """
    Removes special characters from a string.

    Args:
        input_string (str): The input string to clean.

    Returns:
        str: The input string with special characters removed.
    """
    return "".join(char for char in input_string if char.isalnum() or char.isspace())
```
