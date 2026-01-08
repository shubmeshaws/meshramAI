```python
"""
String utility functions for common string operations.
"""

import re

def is_empty(string):
    """
    Checks if a string is empty or contains only whitespace characters.
    
    Args:
        string (str): The input string to check.
    
    Returns:
        bool: True if the string is empty, False otherwise.
    """
    return not string.strip()

def is_valid_email(email):
    """
    Checks if a string is a valid email address.
    
    Args:
        email (str): The input email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def normalize_string(input_string):
    """
    Normalizes a string by converting it to lowercase and removing leading/trailing whitespace.
    
    Args:
        input_string (str): The input string to normalize.
    
    Returns:
        str: The normalized string.
    """
    return input_string.strip().lower()

def truncate_string(input_string, max_length):
    """
    Truncates a string to a specified maximum length.
    
    Args:
        input_string (str): The input string to truncate.
        max_length (int): The maximum length of the output string.
    
    Returns:
        str: The truncated string.
    """
    if len(input_string) > max_length:
        return input_string[:max_length] + "..."
    return input_string
```
