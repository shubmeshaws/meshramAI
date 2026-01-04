```python
"""
String utility module.

This module provides functions for parsing, formatting, and validating strings.
"""

import re

def parse_aws_id(aws_id):
    """
    Parse an AWS ID and extract the resource type and ID.

    Args:
        aws_id (str): The AWS ID to parse.

    Returns:
        tuple: A tuple containing the resource type and ID.
    """
    match = re.match(r"(?P<resource_type>i-|ami-|arn:aws:)[a-zA-Z0-9-]+(?P<resource_id>[a-zA-Z0-9]+)", aws_id)
    if match:
        return match.group("resource_type"), match.group("resource_id")
    return None, None

def format_aws_id(resource_type, resource_id):
    """
    Format an AWS ID from a resource type and ID.

    Args:
        resource_type (str): The resource type.
        resource_id (str): The resource ID.

    Returns:
        str: The formatted AWS ID.
    """
    return f"{resource_type}{resource_id}"

def validate_aws_id(aws_id):
    """
    Validate an AWS ID.

    Args:
        aws_id (str): The AWS ID to validate.

    Returns:
        bool: True if the AWS ID is valid, False otherwise.
    """
    match = re.match(r"(?P<resource_type>i-|ami-|arn:aws:)[a-zA-Z0-9-]+(?P<resource_id>[a-zA-Z0-9]+)", aws_id)
    return bool(match)

def truncate_string(s, max_length):
    """
    Truncate a string to a maximum length.

    Args:
        s (str): The string to truncate.
        max_length (int): The maximum length.

    Returns:
        str: The truncated string.
    """
    if len(s) > max_length:
        return s[:max_length - 3] + "..."
    return s
```
