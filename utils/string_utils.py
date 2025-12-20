```python
import re

def validate_string(input_str, min_length=1, max_length=255):
    """
    Validate a string based on its length.

    Args:
        input_str (str): The input string to validate.
        min_length (int): The minimum allowed length. Defaults to 1.
        max_length (int): The maximum allowed length. Defaults to 255.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    return min_length <= len(input_str) <= max_length

def sanitize_string(input_str):
    """
    Sanitize a string by removing leading/trailing whitespaces and replacing special characters with underscores.

    Args:
        input_str (str): The input string to sanitize.

    Returns:
        str: The sanitized string.
    """
    sanitized_str = input_str.strip()
    sanitized_str = re.sub(r'[^a-zA-Z0-9_]', '_', sanitized_str)
    return sanitized_str

def format_string(input_str, prefix='', suffix=''):
    """
    Format a string by adding a prefix and/or suffix.

    Args:
        input_str (str): The input string to format.
        prefix (str): The prefix to add. Defaults to ''.
        suffix (str): The suffix to add. Defaults to ''.

    Returns:
        str: The formatted string.
    """
    return f"{prefix}{input_str}{suffix}"

def snake_case_to_camel_case(input_str):
    """
    Convert a snake case string to camel case.

    Args:
        input_str (str): The input string to convert.

    Returns:
        str: The converted string.
    """
    components = input_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Example usage
if __name__ == "__main__":
    input_str = "   hello world   "
    print(validate_string(input_str))  # Output: True
    print(sanitize_string(input_str))  # Output: hello_world
    print(format_string(input_str, 'prefix_', '_suffix'))  # Output: prefix_hello_world_suffix
    print(snake_case_to_camel_case('hello_world'))  # Output: helloWorld
```
