```python
import os
import logging

from utils.logging import get_logger

LOGGER = get_logger(__name__)

def get_env_var(var_name):
    """
    Retrieves the value of an environment variable.

    Args:
        var_name (str): The name of the environment variable.

    Returns:
        str: The value of the environment variable, or None if it does not exist.
    """
    return os.environ.get(var_name)

def set_env_var(var_name, var_value):
    """
    Sets the value of an environment variable.

    Args:
        var_name (str): The name of the environment variable.
        var_value (str): The value to set for the environment variable.
    """
    os.environ[var_name] = var_value

def validate_env_vars(required_vars):
    """
    Validates that the required environment variables are set.

    Args:
        required_vars (list): A list of required environment variable names.

    Raises:
        ValueError: If any of the required environment variables are not set.
    """
    for var in required_vars:
        if get_env_var(var) is None:
            LOGGER.error(f"Environment variable '{var}' is not set.")
            raise ValueError(f"Environment variable '{var}' is required.")

def load_env_vars_from_file(file_path):
    """
    Loads environment variables from a file.

    Args:
        file_path (str): The path to the file containing environment variables.

    Returns:
        dict: A dictionary of environment variables loaded from the file.
    """
    env_vars = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    var, value = line.split('=', 1)
                    env_vars[var.strip()] = value.strip()
    except FileNotFoundError:
        LOGGER.error(f"File '{file_path}' not found.")
    return env_vars

def set_env_vars_from_file(file_path):
    """
    Sets environment variables from a file.

    Args:
        file_path (str): The path to the file containing environment variables.
    """
    env_vars = load_env_vars_from_file(file_path)
    for var, value in env_vars.items():
        set_env_var(var, value)
```
