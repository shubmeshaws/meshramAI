```python
import logging
import os

# Set up logging configuration
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')

# Validate the LOGGING_LEVEL environment variable
valid_levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}

if LOGGING_LEVEL.upper() not in valid_levels:
    logging.warning(f"Invalid LOGGING_LEVEL: {LOGGING_LEVEL}. Defaulting to INFO.")
    LOGGING_LEVEL = 'INFO'

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=valid_levels[LOGGING_LEVEL.upper()]
)

class Logger:
    """
    A logger class that handles logging at different levels.

    Attributes:
    name (str): The name of the logger.
    logger (Logger): The underlying logger object.
    log_levels (dict): A dictionary mapping log levels to their corresponding functions.
    """

    def __init__(self, name):
        """
        Initializes a new logger with the given name.

        Args:
        name (str): The name of the logger.
        """
        self.logger = logging.getLogger(name)
        self.log_levels = {
            'INFO': self.logger.info,
            'ERROR': self.logger.error,
            'DEBUG': self.logger.debug,
            'WARNING': self.logger.warning
        }

    def log(self, level, message):
        """
        Logs a message at the specified level.

        Args:
        level (str): The level at which to log the message (INFO, ERROR, DEBUG, WARNING).
        message (str): The message to log.
        """
        level_func = self.log_levels.get(level.upper())
        if level_func:
            level_func(message)
        else:
            logging.warning(f"Invalid log level: {level}")

def get_logger(name):
    """
    Returns a new logger with the given name.

    Args:
    name (str): The name of the logger.

    Returns:
    Logger: A new logger object.
    """
    return Logger(name)

# Example usage:
# logger = get_logger(__name__)
# logger.log('INFO', 'This is an info message')
# logger.log('ERROR', 'This is an error message')
```
