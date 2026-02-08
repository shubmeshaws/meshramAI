```python
"""
String utility functions for meshram project.
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
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def validate_phone_number(phone_number: str) -> bool:
    """
    Validate a phone number.

    Args:
    phone_number (str): The phone number to validate.

    Returns:
    bool: True if the phone number is valid, False otherwise.
    """
    phone_regex = r"^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$"
    return bool(re.match(phone_regex, phone_number))

def remove_special_chars(input_string: str) -> str:
    """
    Remove special characters from a string.

    Args:
    input_string (str): The string to process.

    Returns:
    str: The input string without special characters.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_string)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a specified maximum length.

    Args:
    input_string (str): The string to truncate.
    max_length (int): The maximum length of the string.

    Returns:
    str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
