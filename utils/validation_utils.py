```python
import re

def validate_aws_resource_name(name, max_length=255, min_length=3):
    """
    Validate an AWS resource name.

    Args:
    - name (str): The name of the AWS resource.
    - max_length (int): The maximum length of the name (default: 255).
    - min_length (int): The minimum length of the name (default: 3).

    Returns:
    - bool: True if the name is valid, False otherwise.
    """
    if not isinstance(name, str):
        return False
    if len(name) < min_length or len(name) > max_length:
        return False
    if not re.match("^[a-zA-Z0-9_-]+$", name):
        return False
    return True

def validate_aws_resource_id(id, min_length=1, max_length=128):
    """
    Validate an AWS resource ID.

    Args:
    - id (str): The ID of the AWS resource.
    - min_length (int): The minimum length of the ID (default: 1).
    - max_length (int): The maximum length of the ID (default: 128).

    Returns:
    - bool: True if the ID is valid, False otherwise.
    """
    if not isinstance(id, str):
        return False
    if len(id) < min_length or len(id) > max_length:
        return False
    if not re.match("^[a-zA-Z0-9_-:]+$", id):
        return False
    return True

def validate_aws_region(region):
    """
    Validate an AWS region.

    Args:
    - region (str): The AWS region.

    Returns:
    - bool: True if the region is valid, False otherwise.
    """
    valid_regions = ["us-east-1", "us-east-2", "us-west-1", "us-west-2", "ca-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-central-1", "ap-northeast-1", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "sa-east-1"]
    return region in valid_regions

def validate_aws_bucket_name(name):
    """
    Validate an AWS S3 bucket name.

    Args:
    - name (str): The name of the S3 bucket.

    Returns:
    - bool: True if the name is valid, False otherwise.
    """
    if not isinstance(name, str):
        return False
    if len(name) < 3 or len(name) > 63:
        return False
    if not re.match("^[a-z0-9.-]+$", name):
        return False
    if name[0] == "." or name[-1] == ".":
        return False
    if ".." in name:
        return False
    return True
```
