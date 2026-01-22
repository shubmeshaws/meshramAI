```python
"""
Utility functions for string manipulation and validation.
"""

import re

def is_empty_string(input_string: str) -> bool:
    """
    Checks if a given string is empty or not.

    Args:
    input_string (str): The input string to check.

    Returns:
    bool: True if the string is empty, False otherwise.
    """
    return not input_string.strip()

def is_valid_email(email: str) -> bool:
    """
    Checks if a given email address is valid or not.

    Args:
    email (str): The email address to check.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def snake_case_to_camel_case(input_string: str) -> str:
    """
    Converts a snake_case string to camelCase.

    Args:
    input_string (str): The input string to convert.

    Returns:
    str: The converted camelCase string.
    """
    words = input_string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

def remove_special_characters(input_string: str) -> str:
    """
    Removes all special characters from a given string.

    Args:
    input_string (str): The input string to clean.

    Returns:
    str: The cleaned string with no special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)
```
