import re
from typing import Optional
from datetime import date

from .exceptions import ValidarDatasError


def validar_datas(data: str) -> Optional[date]:
    try:
        regex = re.match(r'^(\d{2})[-/]?(\d{2})[-/]?(\d{4})$', data.strip()).groups()
        return date.fromisoformat(''.join(regex[::-1]))
    except (AttributeError, TypeError, ValueError, IndexError):
        raise ValidarDatasError(valor=data)