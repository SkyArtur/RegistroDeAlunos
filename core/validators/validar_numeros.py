from typing import Optional

from .exceptions import ValidarNumerosError, ValidarNumerosMinnError, ValidarNumerosMaxxError



def validar_numeros(valor: int | float | str, *, minn: Optional[int | float] = None, maxx: Optional[int | float] = None) -> Optional[int | float]:
    try:
        _valor = valor if not isinstance(valor, str) else eval(valor.replace(',', '.'))
        if minn is not None or maxx is not None:
            if minn is not None:
                if not _valor >= minn:
                    raise ValidarNumerosMinnError(valor=valor, minn=minn)
            if maxx is not None:
                if not _valor <= maxx:
                    raise ValidarNumerosMaxxError(valor=valor, maxx=maxx)
        return _valor
    except (ValidarNumerosMaxxError, ValidarNumerosMinnError, NameError, IndexError) as erro:
        if isinstance(erro, NameError) or isinstance(erro, IndexError):
            raise ValidarNumerosError(valor=valor)
        raise