# logger_configuration.py
import logging

LOG_LEVEL = logging.INFO  # default fallback

def set_global_log_level(level):
    global LOG_LEVEL
    LOG_LEVEL = level
    logging.getLogger().setLevel(LOG_LEVEL)

def get_logger(name=None, level=None):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level if level is not None else LOG_LEVEL)
    return logger
