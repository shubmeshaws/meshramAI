```python
import re
import ipaddress

def validate_aws_credentials(access_key, secret_key):
    """
    Validate AWS access key and secret key.

    Args:
    access_key (str): AWS access key.
    secret_key (str): AWS secret key.

    Returns:
    bool: True if credentials are valid, False otherwise.
    """
    if not isinstance(access_key, str) or not isinstance(secret_key, str):
        return False
    if not re.match(r"^(?=[a-zA-Z0-9#]{20}$)(?!.*(__|--|\.){2,}).*$", access_key):
        return False
    if not re.match(r"^(?=[a-zA-Z0-9\/+=]{40}$)(?!.*(__|--|\.){2,}).*$", secret_key):
        return False
    return True

def validate_ip_address(ip):
    """
    Validate an IP address.

    Args:
    ip (str): IP address to validate.

    Returns:
    bool: True if IP address is valid, False otherwise.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_cidr_block(cidr_block):
    """
    Validate a CIDR block.

    Args:
    cidr_block (str): CIDR block to validate.

    Returns:
    bool: True if CIDR block is valid, False otherwise.
    """
    try:
        ipaddress.ip_network(cidr_block, strict=False)
        return True
    except ValueError:
        return False

def validate_region(region):
    """
    Validate an AWS region.

    Args:
    region (str): AWS region to validate.

    Returns:
    bool: True if region is valid, False otherwise.
    """
    valid_regions = ["us-east-1", "us-west-2", "ap-northeast-1", "ap-southeast-1", "eu-west-1"]
    return region in valid_regions
```
