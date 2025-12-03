```python
# utils/validation_utils.py

import re
from datetime import datetime

def validate_email(email):
    """
    Validate an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def validate_ip_address(ip_address):
    """
    Validate an IP address.
    
    Args:
        ip_address (str): The IP address to validate.
    
    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    ip_address_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(ip_address_regex, ip_address))

def validate_date(date_string, date_format="%Y-%m-%d"):
    """
    Validate a date string.
    
    Args:
        date_string (str): The date string to validate.
        date_format (str): The format of the date string.
    
    Returns:
        bool: True if the date string is valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def validate_string_length(input_string, min_length, max_length):
    """
    Validate the length of a string.
    
    Args:
        input_string (str): The string to validate.
        min_length (int): The minimum allowed length.
        max_length (int): The maximum allowed length.
    
    Returns:
        bool: True if the string length is valid, False otherwise.
    """
    return min_length <= len(input_string) <= max_length
```
