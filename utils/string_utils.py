```python
import re
import json

def is_ip_address(ip: str) -> bool:
    """
    Check if a given string is a valid IP address.

    Args:
    ip (str): The IP address to check.

    Returns:
    bool: True if the string is a valid IP address, False otherwise.
    """
    ip_address = re.compile(r'^(?:[0-9]{1,3}.){3}[0-9]{1,3}$')
    return bool(ip_address.match(ip))

def is_valid_json(json_str: str) -> bool:
    """
    Check if a given string is a valid JSON.

    Args:
    json_str (str): The string to check.

    Returns:
    bool: True if the string is a valid JSON, False otherwise.
    """
    try:
        json.loads(json_str)
    except json.JSONDecodeError:
        return False
    return True

def parse_string_to_dict(str_to_parse: str, delimiter: str = ',') -> dict:
    """
    Parse a given string into a dictionary.

    Args:
    str_to_parse (str): The string to parse.
    delimiter (str): The delimiter to use for parsing. Defaults to ','.

    Returns:
    dict: A dictionary representation of the input string.
    """
    result = {}
    for pair in str_to_parse.split(delimiter):
        key_value = pair.split('=')
        if len(key_value) == 2:
            result[key_value[0].strip()] = key_value[1].strip()
    return result

def escape_special_chars(input_str: str) -> str:
    """
    Escape special characters in a given string.

    Args:
    input_str (str): The string to escape.

    Returns:
    str: The input string with special characters escaped.
    """
    return input_str.replace('\\', '\\\\').replace('"', '\\"').replace("'", "\\'")

def unescape_special_chars(input_str: str) -> str:
    """
    Unescape special characters in a given string.

    Args:
    input_str (str): The string to unescape.

    Returns:
    str: The input string with special characters unescaped.
    """
    return input_str.replace('\\\\', '\\').replace('\\"', '"').replace("\\'", "'")
```
