```python
"""
Utility module for common string operations.
"""

import re

def format_string(input_str, prefix=None, suffix=None):
    """
    Format the input string by adding prefix and/or suffix.
    
    Args:
        input_str (str): The input string to be formatted.
        prefix (str, optional): The prefix to be added to the input string. Defaults to None.
        suffix (str, optional): The suffix to be added to the input string. Defaults to None.
    
    Returns:
        str: The formatted string.
    """
    if prefix:
        input_str = prefix + input_str
    if suffix:
        input_str += suffix
    return input_str

def validate_email(email):
    """
    Validate the input email address using a regular expression.
    
    Args:
        email (str): The email address to be validated.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))

def truncate_string(input_str, max_length):
    """
    Truncate the input string to the specified maximum length.
    
    Args:
        input_str (str): The input string to be truncated.
        max_length (int): The maximum length of the output string.
    
    Returns:
        str: The truncated string.
    """
    if len(input_str) > max_length:
        return input_str[:max_length] + "..."
    return input_str

def remove_special_chars(input_str):
    """
    Remove special characters from the input string.
    
    Args:
        input_str (str): The input string to be cleaned.
    
    Returns:
        str: The cleaned string.
    """
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_str)
```
