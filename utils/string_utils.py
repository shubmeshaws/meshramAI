```python
"""
String utility functions.
"""

import re

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def truncate_string(input_str: str, max_length: int) -> str:
    """
    Truncate a string to a specified length.

    Args:
    input_str (str): The input string.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + "..."
    return input_str

def remove_special_chars(input_str: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_str (str): The input string.

    Returns:
    str: The string with special characters removed.
    """
    return re.sub(r"[^a-zA-Z0-9\s]", "", input_str)

def to_snake_case(input_str: str) -> str:
    """
    Convert a string to snake case.

    Args:
    input_str (str): The input string.

    Returns:
    str: The string in snake case.
    """
    return re.sub(r"([A-Z])", r"_\1", input_str).lower().lstrip("_")

def to_camel_case(input_str: str) -> str:
    """
    Convert a string to camel case.

    Args:
    input_str (str): The input string.

    Returns:
    str: The string in camel case.
    """
    words = input_str.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])
```
