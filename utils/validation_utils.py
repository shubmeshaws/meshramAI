```python
import re
import boto3
from utils.error_handling import handle_error

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

def validate_aws_region(region):
    """
    Validate an AWS region.
    
    Args:
    region (str): The AWS region to validate.
    
    Returns:
    bool: True if the region is valid, False otherwise.
    """
    ec2 = boto3.client('ec2')
    try:
        ec2.describe_regions(RegionNames=[region])
        return True
    except Exception as e:
        handle_error(f"Invalid AWS region: {region}. Error: {str(e)}")
        return False

def validate_aws_account_id(account_id):
    """
    Validate an AWS account ID.
    
    Args:
    account_id (str): The AWS account ID to validate.
    
    Returns:
    bool: True if the account ID is valid, False otherwise.
    """
    if not re.match(r'^\d{12}$', account_id):
        return False
    try:
        sts = boto3.client('sts')
        sts.get_caller_identity()
        return True
    except Exception as e:
        handle_error(f"Invalid AWS account ID: {account_id}. Error: {str(e)}")
        return False
```
