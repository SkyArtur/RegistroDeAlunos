from functools import wraps
from typing import Callable

from core.validators.exceptions import ValidadoresError
from core import create_logger
from .exceptions import EntradaTentativasError


logger = create_logger()


def entrada_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(entrada, *, config_tentativas: int = 3, **kwargs):
        tentativas = config_tentativas
        while tentativas > 0:
            try:
                _input = func(input(entrada), **kwargs)
                return _input
            except (ValidadoresError, ) as e:
                mensagem = getattr(e, "message", str(e))
                logger.warning(mensagem)
                tentativas -= 1
        raise EntradaTentativasError(func.__name__)
    return wrapper
