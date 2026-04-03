from pathlib import Path
import random
import sqlite3

import pytest

import database.manager.gerenciador as gerenciador_module
from database import GerenciadorDatabase


@pytest.fixture
def caminho_database_test(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
    arquivo = tmp_path / "db_gerenciador.sqlite"
    monkeypatch.setattr(
        gerenciador_module,
        "caminho_database",
        lambda *, debug=False: arquivo,
    )
    return arquivo

@pytest.fixture
def tabela_nota() -> str:
    return """CREATE TABLE IF NOT EXISTS nota (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor INTEGER NOT NULL
    );"""

@pytest.fixture
def tabela_nota_criada(caminho_database_test: Path, tabela_nota: str) -> None:
    with GerenciadorDatabase(tabela_nota, debug=True) as dbase:
        dbase.create()

def test_gerenciador_database_cria_uma_tabela(caminho_database_test: Path, tabela_nota: str, ) -> None:
    with GerenciadorDatabase(tabela_nota, debug=True) as dbase:
        dbase.create()
        dbase.query = 'SELECT name FROM sqlite_master WHERE type="table" AND name="nota";'
        tabela = dbase.fetch(one=True)
        assert isinstance(tabela, tuple)
        assert len(tabela) == 1
        assert tabela[0] == "nota"


@pytest.mark.parametrize("nota", [pytest.param(random.randint(0, 5_000_000), id="numero inteiro em nota")],)
def test_gerenciador_database_insert_retorna_lastrowid(caminho_database_test: Path, tabela_nota_criada: None, nota: int) -> None:
    with GerenciadorDatabase("INSERT INTO nota (valor) VALUES (?)", (nota,), debug=True) as dbase:
        id_nota = dbase.alter()
    with GerenciadorDatabase("SELECT * FROM nota WHERE id = ?", (id_nota,), debug=True) as dbase:
        confirmar_nota = dbase.fetch(one=True)
    assert isinstance(id_nota, int)
    assert isinstance(confirmar_nota, tuple)
    assert confirmar_nota[0] == id_nota
    assert confirmar_nota[1] == nota


@pytest.mark.parametrize("nota", [pytest.param("a", id="valor textual em coluna integer")],)
def test_gerenciador_database_sqlite_aceita_texto_em_coluna_integer(caminho_database_test: Path, tabela_nota_criada: None, nota: str,) -> None:
    with GerenciadorDatabase("INSERT INTO nota (valor) VALUES (?)", (nota,), debug=True) as dbase:
        id_nota = dbase.alter()
    with GerenciadorDatabase("SELECT valor, typeof(valor) FROM nota WHERE id = ?", (id_nota,), debug=True,) as dbase:
        valor_salvo = dbase.fetch(one=True)
    assert isinstance(id_nota, int)
    assert valor_salvo == (nota, "text")


def test_gerenciador_de_contexto_database_abre_e_fecha_conexao(caminho_database_test: Path,) -> None:
    with GerenciadorDatabase("SELECT 1;", debug=True) as dbase:
        retorno = dbase.fetch(one=True)
        assert isinstance(retorno, tuple)
    with pytest.raises(sqlite3.ProgrammingError):
        dbase.fetch(one=True)
