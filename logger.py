import logging

log_filename = "app.log"


def logger_setup():
    logger = logging.getLogger("commit-generator")
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_filename, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


log = logger_setup()
