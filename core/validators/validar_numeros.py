from typing import Optional

from .exceptions import ValidarNumerosError, ValidarNumerosMinnError, ValidarNumerosMaxxError


def _converter_texto_para_numero(valor: str) -> int | float:
    """Converte uma representação textual simples para número.

    Args:
        valor: Texto representando um número inteiro ou decimal.

    Returns:
        O valor convertido para ``int`` ou ``float``.

    Raises:
        ValueError: Quando o texto informado não representa um número válido.
    """
    valor_normalizado = valor.strip().replace(',', '.')
    if '.' in valor_normalizado:
        return float(valor_normalizado)
    return int(valor_normalizado)



def validar_numeros(valor: int | float | str, *, minn: Optional[int | float] = None, maxx: Optional[int | float] = None) -> int | float:
    """Valida se o valor informado representa um numero aceitável.

    Args:
        valor: Valor a ser validado, aceitando numero ou representacao textual.
        minn: Limite minimo aceito para o valor informado.
        maxx: Limite maximo aceito para o valor informado.

    Returns:
        O valor convertido e validado quando atender aos criterios definidos.

    Raises:
        ValidarNumerosError: Quando o valor informado nao representa um numero valido.
        ValidarNumerosMinnError: Quando o valor for menor que o limite minimo.
        ValidarNumerosMaxxError: Quando o valor for maior que o limite maximo.
    """
    detalhe = str(validar_numeros.__name__)
    try:
        _valor = valor if not isinstance(valor, str) else _converter_texto_para_numero(valor)
        if minn is not None or maxx is not None:
            if minn is not None:
                if not _valor >= minn:
                    raise ValidarNumerosMinnError(valor, minn=minn, detalhe=detalhe)
            if maxx is not None:
                if not _valor <= maxx:
                    raise ValidarNumerosMaxxError(valor, maxx=maxx, detalhe=detalhe)
        return _valor
    except (ValidarNumerosMaxxError, ValidarNumerosMinnError, ValueError, TypeError) as erro:
        if isinstance(erro, ValueError) or isinstance(erro, TypeError):
            raise ValidarNumerosError(valor, detalhe=detalhe)
        raise
