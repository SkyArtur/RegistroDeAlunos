import logging

from .formatter import ColorFormatter, SafeExtraFormatter


def create_logger():
    """Cria e configura a instância principal de logger do projeto.

    Returns:
        A instância de logger configurada para saída em console e arquivo.
    """
    logger = logging.getLogger("colorido")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(
            ColorFormatter("[%(levelname)s] - %(message)s < %(detalhe)s >")
        )
        file_handler = logging.FileHandler("app.log", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            SafeExtraFormatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s < %(detalhe)s >"
            )
        )
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    return logger
