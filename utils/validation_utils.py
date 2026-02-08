```python
import re
import ipaddress
from urllib.parse import urlparse

def validate_ip_address(ip_address):
    """
    Validate an IP address.

    Args:
    ip_address (str): The IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

def validate_url(url):
    """
    Validate a URL.

    Args:
    url (str): The URL to validate.

    Returns:
    bool: True if the URL is valid, False otherwise.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def validate_aws_resource_name(name, resource_type):
    """
    Validate an AWS resource name.

    Args:
    name (str): The resource name to validate.
    resource_type (str): The type of AWS resource (e.g., 'vpc', 'subnet', 'sg').

    Returns:
    bool: True if the resource name is valid, False otherwise.
    """
    if resource_type == 'vpc':
        # VPC names can be up to 255 characters long and can contain letters, numbers, and special characters
        pattern = r'^[a-zA-Z0-9._-]{1,255}$'
    elif resource_type == 'subnet':
        # Subnet names can be up to 255 characters long and can contain letters, numbers, and special characters
        pattern = r'^[a-zA-Z0-9._-]{1,255}$'
    elif resource_type == 'sg':
        # Security group names can be up to 255 characters long and can contain letters, numbers, and special characters
        pattern = r'^[a-zA-Z0-9._-]{1,255}$'
    else:
        raise ValueError(f"Unsupported resource type: {resource_type}")

    return bool(re.match(pattern, name))

# Example usage:
if __name__ == "__main__":
    print(validate_ip_address("192.168.1.1"))  # True
    print(validate_url("https://www.example.com"))  # True
    print(validate_aws_resource_name("my-vpc", "vpc"))  # True
```
