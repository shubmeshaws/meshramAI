```python
import re
import ipaddress
from urllib.parse import urlparse

def is_valid_ip_address(ip_address):
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

def is_valid_url(url):
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

def is_valid_aws_resource_id(resource_id):
    """
    Validate an AWS resource ID.
    
    Args:
        resource_id (str): The AWS resource ID to validate.
    
    Returns:
        bool: True if the AWS resource ID is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9\-_]+$'
    return bool(re.match(pattern, resource_id))

def is_valid_aws_region(region):
    """
    Validate an AWS region.
    
    Args:
        region (str): The AWS region to validate.
    
    Returns:
        bool: True if the AWS region is valid, False otherwise.
    """
    # List of valid AWS regions
    valid_regions = ['us-east-1', 'us-west-2', 'us-west-1', 'eu-west-1', 'eu-central-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'sa-east-1']
    return region in valid_regions

# Example usage:
if __name__ == '__main__':
    print(is_valid_ip_address('192.168.1.1'))  # True
    print(is_valid_url('https://www.example.com'))  # True
    print(is_valid_aws_resource_id('i-0123456789abcdef0'))  # True
    print(is_valid_aws_region('us-east-1'))  # True
```
