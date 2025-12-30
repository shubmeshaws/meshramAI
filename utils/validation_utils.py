```python
import re
from typing import Optional

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

def validate_aws_resource_id(resource_id: str) -> bool:
    """
    Validate an AWS resource ID.
    
    Args:
    resource_id (str): The AWS resource ID to validate.
    
    Returns:
    bool: True if the resource ID is valid, False otherwise.
    """
    # AWS resource IDs are typically in the format of xxx-xxxxxxx-xxxxxxx
    resource_id_regex = r"^[a-zA-Z0-9]{1,64}(-[a-zA-Z0-9]{1,64})+$"
    return bool(re.match(resource_id_regex, resource_id))

def validate_aws_region(region: str) -> bool:
    """
    Validate an AWS region.
    
    Args:
    region (str): The AWS region to validate.
    
    Returns:
    bool: True if the region is valid, False otherwise.
    """
    # AWS regions are typically in the format of xxx-xxxx-xx
    region_regex = r"^[a-z]{2}-[a-z]+-[0-9a-z]+$"
    return bool(re.match(region_regex, region))

def validate_ip_address(ip_address: str) -> bool:
    """
    Validate an IP address.
    
    Args:
    ip_address (str): The IP address to validate.
    
    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    # IP addresses are typically in the format of xxx.xxx.xxx.xxx
    ip_address_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_address_regex, ip_address))

def validate_string_length(input_string: str, min_length: int = 1, max_length: int = 255) -> bool:
    """
    Validate the length of a string.
    
    Args:
    input_string (str): The string to validate.
    min_length (int): The minimum allowed length. Defaults to 1.
    max_length (int): The maximum allowed length. Defaults to 255.
    
    Returns:
    bool: True if the string length is valid, False otherwise.
    """
    return min_length <= len(input_string) <= max_length

def validate_optional_string(input_string: Optional[str]) -> bool:
    """
    Validate an optional string.
    
    Args:
    input_string (Optional[str]): The string to validate.
    
    Returns:
    bool: True if the string is valid or None, False otherwise.
    """
    return input_string is None or isinstance(input_string, str)
```
