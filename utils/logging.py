```python
import logging
import os

# Set up logging configuration
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')

# Validate the LOGGING_LEVEL environment variable
valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
if LOGGING_LEVEL.upper() not in valid_levels:
    logging.warning(f"Invalid LOGGING_LEVEL: {LOGGING_LEVEL}. Defaulting to INFO.")
    LOGGING_LEVEL = 'INFO'

try:
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=getattr(logging, LOGGING_LEVEL.upper())
    )
except Exception as e:
    logging.error(f"Error setting up logging: {str(e)}")
    raise

class Logger:
    def __init__(self, name):
        try:
            self.logger = logging.getLogger(name)
        except Exception as e:
            logging.error(f"Error creating logger: {str(e)}")
            raise

    def _log(self, level, message):
        try:
            level_func = getattr(self.logger, level)
            level_func(message)
        except Exception as e:
            logging.error(f"Error logging {level} message: {str(e)}")
            raise

    def info(self, message):
        self._log('info', message)

    def error(self, message):
        self._log('error', message)

    def debug(self, message):
        self._log('debug', message)

    def warn(self, message):
        self._log('warning', message)

def get_logger(name):
    return Logger(name)

# Example usage:
# logger = get_logger(__name__)
# logger.info('This is an info message')
# logger.error('This is an error message')
```
