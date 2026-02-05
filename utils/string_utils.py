```python
"""
String utility functions.
"""

import re

def format_string(input_str, **kwargs):
    """
    Replaces placeholders in the input string with the provided keyword arguments.
    
    Args:
    input_str (str): The input string containing placeholders.
    **kwargs: Keyword arguments to replace the placeholders.
    
    Returns:
    str: The formatted string.
    """
    return input_str.format(**kwargs)

def validate_email(email):
    """
    Validates if the input string is a valid email address.
    
    Args:
    email (str): The input string to be validated.
    
    Returns:
    bool: True if the input string is a valid email address, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def truncate_string(input_str, max_length):
    """
    Truncates the input string to the specified maximum length.
    
    Args:
    input_str (str): The input string to be truncated.
    max_length (int): The maximum length of the output string.
    
    Returns:
    str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length - 3] + "..."
    return input_str

def remove_special_chars(input_str):
    """
    Removes special characters from the input string.
    
    Args:
    input_str (str): The input string containing special characters.
    
    Returns:
    str: The input string with special characters removed.
    """
    return re.sub('[^A-Za-z0-9]+', '', input_str)
```
