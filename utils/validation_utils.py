```python
import re

def validate_string(input_string, min_length=1, max_length=255):
    """
    Validate a string.

    Args:
        input_string (str): The string to validate.
        min_length (int, optional): The minimum allowed length. Defaults to 1.
        max_length (int, optional): The maximum allowed length. Defaults to 255.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    if not isinstance(input_string, str):
        return False
    if len(input_string) < min_length or len(input_string) > max_length:
        return False
    return True

def validate_integer(input_integer, min_value=None, max_value=None):
    """
    Validate an integer.

    Args:
        input_integer (int): The integer to validate.
        min_value (int, optional): The minimum allowed value. Defaults to None.
        max_value (int, optional): The maximum allowed value. Defaults to None.

    Returns:
        bool: True if the integer is valid, False otherwise.
    """
    if not isinstance(input_integer, int):
        return False
    if min_value is not None and input_integer < min_value:
        return False
    if max_value is not None and input_integer > max_value:
        return False
    return True

def validate_aws_resource_name(input_string):
    """
    Validate an AWS resource name.

    Args:
        input_string (str): The resource name to validate.

    Returns:
        bool: True if the resource name is valid, False otherwise.
    """
    pattern = re.compile(r'^[a-zA-Z0-9-]+$')
    if not pattern.match(input_string):
        return False
    if len(input_string) < 1 or len(input_string) > 255:
        return False
    return True

def validate_aws_tag_key(input_string):
    """
    Validate an AWS tag key.

    Args:
        input_string (str): The tag key to validate.

    Returns:
        bool: True if the tag key is valid, False otherwise.
    """
    pattern = re.compile(r'^[a-zA-Z0-9-_]+$')
    if not pattern.match(input_string):
        return False
    if len(input_string) < 1 or len(input_string) > 128:
        return False
    return True
```
