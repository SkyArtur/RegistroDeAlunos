from datetime import date

import pytest

from core import entrada_datas, entrada_numeros, entrada_padrao
from core.inputs.exceptions import EntradaTentativasError


@pytest.mark.parametrize(
    "valor,tipo",
    [
        pytest.param(12, int, id="entrada valida de tipo int"),
        pytest.param(1.2, float, id="entrada valida de tipo float"),
        pytest.param("12", int, id="entrada valida de tipo string"),
    ],
)
def test_integracao_entrada_numerica_e_validar_numeros(valor, tipo, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: valor)

    numero = entrada_numeros("Digite um numero inteiro: ")

    assert numero == tipo(valor)
    assert type(numero) is tipo


@pytest.mark.parametrize(
    "valor",
    [
        pytest.param("12/02/2000", id="data com separadores /"),
        pytest.param("12-02-2000", id="data com separadores -"),
        pytest.param("12022000", id="data sem separadores"),
    ],
)
def test_integracao_entrada_datas_e_validar_datas(valor, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: valor)

    data = entrada_datas("Digite uma data: ")

    assert type(data) is date


def test_entrada_padrao_retorna_texto_sem_transformacao(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "texto livre")

    valor = entrada_padrao("Digite qualquer valor: ")

    assert valor == "texto livre"
    assert type(valor) is str


def test_entrada_numeros_repete_ate_receber_um_valor_valido(monkeypatch):
    entradas = iter(["abc", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    numero = entrada_numeros("Digite um numero: ")

    assert numero == 10
    assert type(numero) is int


def test_entrada_numeros_aplica_limites_do_validador(monkeypatch):
    entradas = iter(["2", "8"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    numero = entrada_numeros("Digite um numero entre 5 e 10: ", minn=5, maxx=10)

    assert numero == 8


def test_entrada_datas_repete_ate_receber_uma_data_valida(monkeypatch):
    entradas = iter(["31/02/2020", "12/02/2000"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    data = entrada_datas("Digite uma data: ")

    assert data == date(2000, 2, 12)


def test_entrada_numeros_lanca_erro_quando_excede_tentativas(monkeypatch):
    entradas = iter(["a", "b", "c"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    with pytest.raises(EntradaTentativasError) as exc_info:
        entrada_numeros("Digite um numero: ", config_tentativas=3)

    assert exc_info.value.detalhe == "entrada_numeros"
    assert str(exc_info.value) == "Função <entrada_numeros> excedeu o número máximo de chamadas"


def test_entrada_datas_lanca_erro_quando_excede_tentativas(monkeypatch):
    entradas = iter(["99/99/9999", "texto"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    with pytest.raises(EntradaTentativasError) as exc_info:
        entrada_datas("Digite uma data: ", config_tentativas=2)

    assert exc_info.value.detalhe == "entrada_datas"
