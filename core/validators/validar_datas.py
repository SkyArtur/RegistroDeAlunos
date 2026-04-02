import re
from typing import Optional
from datetime import date

from .exceptions import ValidarDatasError


def validar_datas(data: str) -> Optional[date]:
    """Valida uma data textual e a converte para o tipo ``date``.

    Args:
        data: Data informada em formato textual, com ou sem separadores.

    Returns:
        A data convertida para ``date`` quando o valor informado for valido.

    Raises:
        ValidarDatasError: Quando o texto informado não representa uma data valida.
    """
    try:
        regex = re.match(r'^(\d{2})[-/]?(\d{2})[-/]?(\d{4})$', data.strip()).groups()
        return date.fromisoformat(''.join(regex[::-1]))
    except (AttributeError, TypeError, ValueError, IndexError):
        raise ValidarDatasError(valor=data)
