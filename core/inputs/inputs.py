from datetime import date

from .decorator import entrada_decorator
from core.validators import validar_numeros, validar_datas

@entrada_decorator
def entrada_numeros(entrada: str, **kwargs) -> float | int:
    return validar_numeros(entrada, **kwargs)

@entrada_decorator
def entrada_datas(entrada: str) -> date:
    return validar_datas(entrada)

@entrada_decorator
def entrada_padrao(entrada: str) -> str:
    return entrada
