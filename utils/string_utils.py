```python
"""
String utility functions for general string operations.
"""

import re

def is_empty_string(input_string):
    """
    Checks if the input string is empty or contains only whitespace characters.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()

def validate_email(email):
    """
    Validates an email address using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def remove_special_chars(input_string):
    """
    Removes special characters from the input string.

    Args:
        input_string (str): The input string to remove special characters from.

    Returns:
        str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def truncate_string(input_string, max_length):
    """
    Truncates the input string to the specified maximum length.

    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.

    Returns:
        str: The truncated input string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
