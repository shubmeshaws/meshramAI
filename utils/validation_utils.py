```python
# utils/validation_utils.py

import re
from typing import Any

def validate_string(input_str: str) -> bool:
    """
    Validate if the input is a non-empty string.
    
    Args:
    input_str (str): The input string to be validated.
    
    Returns:
    bool: True if the input is a non-empty string, False otherwise.
    """
    return isinstance(input_str, str) and input_str.strip() != ""

def validate_email(email: str) -> bool:
    """
    Validate if the input is a valid email address.
    
    Args:
    email (str): The email address to be validated.
    
    Returns:
    bool: True if the input is a valid email address, False otherwise.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(email_regex, email))

def validate_aws_region(region: str) -> bool:
    """
    Validate if the input is a valid AWS region.
    
    Args:
    region (str): The AWS region to be validated.
    
    Returns:
    bool: True if the input is a valid AWS region, False otherwise.
    """
    # Load valid AWS regions from regions.conf
    with open("regions.conf", "r") as f:
        valid_regions = [line.strip() for line in f.readlines()]
    
    return region in valid_regions

def validate_input(input_value: Any, input_type: type) -> bool:
    """
    Validate if the input matches the expected data type.
    
    Args:
    input_value (Any): The input value to be validated.
    input_type (type): The expected data type.
    
    Returns:
    bool: True if the input matches the expected data type, False otherwise.
    """
    return isinstance(input_value, input_type)
```
