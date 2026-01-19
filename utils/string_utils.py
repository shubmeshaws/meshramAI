```python
# utils/string_utils.py

"""
Utility functions for string manipulation and validation.
"""

def is_empty_string(input_string: str) -> bool:
    """
    Check if a string is empty or contains only whitespace characters.

    Args:
    input_string (str): The string to check.

    Returns:
    bool: True if the string is empty or contains only whitespace characters, False otherwise.
    """
    return not input_string.strip()

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    import re
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def normalize_string(input_string: str) -> str:
    """
    Normalize a string by converting it to lowercase and removing leading/trailing whitespace.

    Args:
    input_string (str): The string to normalize.

    Returns:
    str: The normalized string.
    """
    return input_string.strip().lower()

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
