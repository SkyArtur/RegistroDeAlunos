from datetime import date

import pytest

from core import validar_datas, validar_numeros
from core.validators.exceptions import (
    ValidarDatasError,
    ValidarNumerosError,
    ValidarNumerosMaxxError,
    ValidarNumerosMinnError,
)


@pytest.mark.parametrize(
    ("entrada", "esperado"),
    [
        pytest.param("21/02/2003", date(2003, 2, 21), id="barra"),
        pytest.param("21-02-2003", date(2003, 2, 21), id="hifen"),
        pytest.param("21-02/2003", date(2003, 2, 21), id="separadores-mistos"),
        pytest.param("21022003", date(2003, 2, 21), id="sem-separador"),
        pytest.param(" 21/02/2003 ", date(2003, 2, 21), id="com-espacos"),
    ],
)
def test_validar_datas_retorna_date_correspondente(entrada, esperado):
    """Garante que entradas de data válidas sejam convertidas corretamente para ``date``."""
    resultado = validar_datas(entrada)

    assert isinstance(resultado, date)
    assert resultado == esperado


@pytest.mark.parametrize(
    "entrada",
    [
        pytest.param("31/02/2003", id="dia-invalido"),
        pytest.param("22-2003", id="faltando-mes"),
        pytest.param("n1-02/2003", id="caracter-nao-numerico"),
        pytest.param(None, id="none"),
        pytest.param("", id="vazio"),
    ],
)
def test_validar_datas_lanca_erro_para_entradas_invalidas(entrada):
    """Verifica que entradas inválidas de data disparem a exceção esperada."""
    with pytest.raises(ValidarDatasError, match=f'Data inválida: {entrada}'):
        validar_datas(entrada)


@pytest.mark.parametrize(
    ("entrada", "tipo_esperado", "valor_esperado"),
    [
        pytest.param(12, int, 12, id="int"),
        pytest.param(22.6, float, 22.6, id="float"),
        pytest.param("103", int, 103, id="str-int"),
        pytest.param("32.6", float, 32.6, id="str-float-ponto"),
        pytest.param("32,6", float, 32.6, id="str-float-virgula"),
        pytest.param(" 42 ", int, 42, id="str-com-espacos"),
    ],
)
def test_validar_numeros_retorna_tipo_e_valor_esperados(entrada, tipo_esperado, valor_esperado):
    """Confirma a conversão numérica preservando tipo esperado e valor final."""
    resultado = validar_numeros(entrada)

    assert not isinstance(resultado, str)
    assert type(resultado) is tipo_esperado
    assert resultado == valor_esperado


@pytest.mark.parametrize(
    "entrada",
    [
        pytest.param("s25", id="texto-com-prefixo"),
        pytest.param("ssd", id="texto-puro"),
        pytest.param("", id="vazio"),
    ],
)
def test_validar_numeros_lanca_erro_para_entradas_invalidas(entrada):
    """Assegura que textos não numéricos resultem em erro de validação numérica."""
    with pytest.raises(ValidarNumerosError, match=r"Valor \[{}\] não é um número válido".format(entrada)):
        validar_numeros(entrada)


def test_validar_numeros_respeita_limite_minimo_e_retorna_valor_no_limite():
    """Valida que um valor exatamente no mínimo permitido seja aceito."""
    resultado = validar_numeros("12", minn=12)

    assert type(resultado) is int
    assert resultado == 12


def test_validar_numeros_lanca_erro_quando_valor_e_menor_que_minimo():
    """Verifica o erro específico quando o valor fica abaixo do limite mínimo."""
    with pytest.raises(ValidarNumerosMinnError, match=r"Valor \[10\] menor que o mínimo \[12\]"):
        validar_numeros("10", minn=12)


def test_validar_numeros_respeita_limite_maximo_e_retorna_valor_no_limite():
    """Valida que um valor exatamente no máximo permitido seja aceito."""
    resultado = validar_numeros("12", maxx=12)

    assert type(resultado) is int
    assert resultado == 12


def test_validar_numeros_lanca_erro_quando_valor_e_maior_que_maximo():
    """Verifica o erro específico quando o valor excede o limite máximo."""
    with pytest.raises(ValidarNumerosMaxxError, match=r"Valor \[13\] maior que o máximo \[12\]"):
        validar_numeros("13", maxx=12)


def test_validar_numeros_aplica_limites_minimo_e_maximo_na_mesma_validacao():
    """Confirma que a validação aceita valores dentro da faixa mínima e máxima."""
    resultado = validar_numeros("10", minn=5, maxx=10)

    assert type(resultado) is int
    assert resultado == 10


def test_validar_numeros_lanca_erro_de_minimo_antes_de_validar_maximo():
    """Documenta a precedência atual da validação de mínimo quando ambos os limites são usados."""
    with pytest.raises(ValidarNumerosMinnError, match=r"Valor \[4\] menor que o mínimo \[5\]"):
        validar_numeros("4", minn=5, maxx=3)
