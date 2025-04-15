import logging

def get_logger(name=None, level=logging.INFO):
    logger = logging.getLogger(name)
    root_logger = logging.getLogger()
    if not root_logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        root_logger.addHandler(handler)

    logger.setLevel(level)
    return logger

