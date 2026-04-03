import logging

from .formatter import ColorFormatter, SafeExtraFormatter, SafeColorFormatter
from .filter import LevelFilter


def create_logger():
    """Cria e configura a instância principal de logger do projeto.

    Returns:
        A instância de logger configurada para saída em console e arquivo.
    """
    logger = logging.getLogger("colorido")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if logger.handlers:
        return logger


    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.addFilter(LevelFilter(only=logging.INFO))
    console_handler.setFormatter(SafeColorFormatter("%(message)s"))

    warning_console_handler = logging.StreamHandler()
    warning_console_handler.setLevel(logging.DEBUG)
    warning_console_handler.addFilter(LevelFilter(only=logging.WARNING))
    warning_console_handler.setFormatter(SafeColorFormatter("[%(levelname)s] - %(message)s"))

    error_console_handler = logging.StreamHandler()
    error_console_handler.setLevel(logging.DEBUG)
    error_console_handler.addFilter(LevelFilter(min_level=logging.ERROR))
    error_console_handler.setFormatter(SafeColorFormatter("[%(levelname)s] - %(message)s  < %(detalhe)s >"))

    file_handler = logging.FileHandler("app.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.addFilter(LevelFilter(min_level=logging.WARNING, max_level=logging.ERROR))
    file_handler.setFormatter(SafeExtraFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s < %(detalhe)s >"))

    logger.addHandler(console_handler)
    logger.addHandler(error_console_handler)
    logger.addHandler(warning_console_handler)
    logger.addHandler(file_handler)
    return logger

