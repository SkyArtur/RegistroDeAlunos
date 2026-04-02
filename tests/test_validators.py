from datetime import date

import pytest

from core import validar_datas, validar_numeros
from core.validators.exceptions import (
    ValidarDatasError,
    ValidarNumerosError,
    ValidarNumerosMaxxError,
    ValidarNumerosMinnError,
)


@pytest.mark.parametrize('data_valida', [
    pytest.param('21/02/2003', id='21/02/2003 -> type(date)'),
    pytest.param('21-02-2003', id='21-02-2003 -> type(date)'),
    pytest.param('21-02/2003', id='21-02/2003 -> type(date)'),
    pytest.param('21022003', id='21022003 -> type(date)'),
])
def test_validar_data_retorna_tipo_date(data_valida):
    assert isinstance(validar_datas(data_valida), date)


@pytest.mark.parametrize('data_invalida', [
    pytest.param('31/02/2003', id='31/02/2003 -> ValidarDataError'),
    pytest.param('22-2003', id='22-2003 -> ValidarDataError'),
    pytest.param('n1-02/2003', id='n1-02/2003 -> ValidarDataError'),
])
def test_erro_validar_data(data_invalida):
    with pytest.raises(ValidarDatasError) as exc_info:
        validar_datas(data_invalida)
    assert 'Data inválida' in str(exc_info.value)

@pytest.mark.parametrize('entrada, tipo_esperado', [
    pytest.param(12, int, id='int(12) -> int'),
    pytest.param(22.6, float, id='float(22.6) -> float'),
    pytest.param('103', int, id='str(103) -> int'),
    pytest.param('32.6', float, id='str(32.6) -> float'),
    pytest.param('32,6', float, id='str(32,6) -> float'),
])
def test_validar_numerico_retorna_tipo_numerico(entrada, tipo_esperado):
    _entrada = validar_numeros(entrada)
    _valor_esperado = tipo_esperado(entrada if not isinstance(entrada, str) else entrada.replace(',', '.'))
    assert not isinstance(_entrada, str)
    assert type(_entrada) is tipo_esperado
    assert _entrada == _valor_esperado

@pytest.mark.parametrize('entrada', [
    pytest.param('s25', id='str(s25) -> ValidarNumeroError'),
    pytest.param('ssd', id='str(ssd) -> ValidarNumeroError'),
])
def test_erro_validar_numerico(entrada):
    with pytest.raises(ValidarNumerosError) as exc_info:
        validar_numeros(entrada)
    assert 'Valor não é um número válido' in str(exc_info.value)

@pytest.mark.parametrize('entrada_valida, entrada_invalida, minn', [
    pytest.param('12', '10', 12, id='(valido=12, invalido=10, minn=12) -> int -> ValidarNumeroMinnError'),
])
def test_validar_numerico_error_minn(entrada_valida, entrada_invalida, minn):
    _entrada = validar_numeros(entrada_valida, minn=minn)
    assert type(_entrada) is int
    assert _entrada == int(entrada_valida)
    with pytest.raises(ValidarNumerosMinnError) as exc_info:
        validar_numeros(entrada_invalida, minn=minn)
    assert f"Valor menor que o mínimo [{minn}]" in str(exc_info.value)

@pytest.mark.parametrize("entrada_valida, entrada_invalida, maxx", [
    pytest.param('12', '13', 12, id='(valido=12, invalido=13, maxx=12) -> int -> ValidarNumeroMaxxError'),
])
def test_validar_numerico_error_maxx(entrada_valida, entrada_invalida, maxx):
    _entrada = validar_numeros(entrada_valida, maxx=maxx)
    assert type(_entrada) is int
    assert _entrada == int(entrada_valida)
    with pytest.raises(ValidarNumerosMaxxError) as exc_info:
        validar_numeros(entrada_invalida, maxx=maxx)
    assert f"Valor maior que [{maxx}]" in str(exc_info.value)
