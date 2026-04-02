import pytest
from datetime import date

from core import validar_datas, validar_numeros
from core.validators.exceptions import (
    ValidarDatasError,
    ValidarNumerosError,
    ValidarNumerosMinnError,
    ValidarNumerosMaxxError
)