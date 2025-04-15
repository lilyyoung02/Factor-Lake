# LoggerConfiguration.py

import logging
import sys

def setup_root_logger(level=logging.INFO):
    """
    Ensure the root logger has a handler and set its level.
    This should be called once from main.py after parsing verbosity.
    """
    root_logger = logging.getLogger()
    if not root_logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('[%(name)s] %(levelname)s: %(message)s')
        handler.setFormatter(handler)
        root_logger.addHandler(handler)
    root_logger.setLevel(level)

def get_logger(name=None):
    """
    Returns a logger instance for the given module name.
    Does not modify logger level; inherits from root.
    """
    return logging.getLogger(name)
