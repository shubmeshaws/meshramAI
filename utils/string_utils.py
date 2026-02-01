```python
# utils/string_utils.py

import re

def is_empty_string(input_string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace characters.

    Args:
    input_string (str): The input string to be checked.

    Returns:
    bool: True if the string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validate an email address using a regular expression.

    Args:
    email (str): The email address to be validated.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_string (str): The input string to be truncated.
    max_length (int): The maximum length of the output string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string

def remove_special_chars(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_string (str): The input string to be processed.

    Returns:
    str: The string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9\s]+', '', input_string)

def to_title_case(input_string: str) -> str:
    """
    Convert a string to title case.

    Args:
    input_string (str): The input string to be converted.

    Returns:
    str: The string in title case.
    """
    return input_string.title()
```
