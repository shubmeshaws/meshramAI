```python
"""
String utility functions.
"""

import re

def to_title_case(input_string: str) -> str:
    """
    Convert a string to title case.

    Args:
        input_string (str): The input string to convert.

    Returns:
        str: The input string in title case.
    """
    return input_string.title()


def remove_special_chars(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
        input_string (str): The input string to process.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9\s]+', '', input_string)


def trim_whitespace(input_string: str) -> str:
    """
    Trim whitespace from the start and end of a string.

    Args:
        input_string (str): The input string to process.

    Returns:
        str: The input string with whitespace trimmed.
    """
    return input_string.strip()


def remove_empty_lines(input_string: str) -> str:
    """
    Remove empty lines from a string.

    Args:
        input_string (str): The input string to process.

    Returns:
        str: The input string with empty lines removed.
    """
    return '\n'.join(line for line in input_string.split('\n') if line.strip() != '')
```
