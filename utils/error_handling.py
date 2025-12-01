```python
import logging
from logging import Logger
from typing import Any, Dict

from utils.logging import get_logger

def handle_error(logger: Logger, error: Exception, error_message: str, error_data: Dict[str, Any] = None) -> None:
    """
    Handle and log an error in a standardized way.

    Args:
        logger (Logger): The logger instance to use.
        error (Exception): The error that occurred.
        error_message (str): A human-readable error message.
        error_data (Dict[str, Any], optional): Additional error data. Defaults to None.
    """
    logger.error(error_message, exc_info=error)

    if error_data:
        logger.error("Error data: %s", error_data)

def log_and_raise(logger: Logger, error_message: str, error_data: Dict[str, Any] = None) -> None:
    """
    Log an error and raise an exception.

    Args:
        logger (Logger): The logger instance to use.
        error_message (str): A human-readable error message.
        error_data (Dict[str, Any], optional): Additional error data. Defaults to None.
    """
    logger.error(error_message)

    if error_data:
        logger.error("Error data: %s", error_data)

    raise Exception(error_message)

def main():
    logger = get_logger(__name__)

    try:
        # Simulate an error
        raise ValueError("Test error")
    except Exception as e:
        handle_error(logger, e, "An error occurred")

if __name__ == "__main__":
    main()
```
