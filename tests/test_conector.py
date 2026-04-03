import sqlite3
from pathlib import Path

import pytest

from database.connector import Conector


def test_conector_retorna_cursor_sqlite(caminho_database_test: Path) -> None:
    conexao = Conector(arquivo=caminho_database_test)
    cursor = conexao.cursor()
    assert isinstance(cursor, sqlite3.Cursor)
    conexao.close()


def test_conector_aceita_caminho_como_string(caminho_database_test: Path) -> None:
    conexao = Conector(arquivo=str(caminho_database_test))
    cursor = conexao.cursor()
    assert isinstance(cursor, sqlite3.Cursor)
    conexao.close()


def test_conector_commit_persiste_dados(caminho_database_test: Path) -> None:
    conexao = Conector(arquivo=caminho_database_test)
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE exemplo (valor INTEGER);")
    cursor.execute("INSERT INTO exemplo (valor) VALUES (10);")
    conexao.commit()
    conexao.close()
    nova_conexao = Conector(arquivo=caminho_database_test)
    novo_cursor = nova_conexao.cursor()
    resultado = novo_cursor.execute("SELECT valor FROM exemplo;").fetchone()
    assert resultado == (10,)
    nova_conexao.close()


def test_conector_rollback_desfaz_alteracoes_nao_confirmadas(caminho_database_test: Path) -> None:
    conexao = Conector(arquivo=caminho_database_test)
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE exemplo (valor INTEGER);")
    conexao.commit()
    cursor.execute("INSERT INTO exemplo (valor) VALUES (10);")
    conexao.rollback()
    resultado = cursor.execute("SELECT valor FROM exemplo;").fetchall()
    assert resultado == []
    conexao.close()


def test_conector_close_invalida_a_conexao(caminho_database_test: Path) -> None:
    conexao = Conector(arquivo=caminho_database_test)
    conexao.close()
    with pytest.raises(sqlite3.ProgrammingError):
        conexao.conexao.execute("SELECT 1;")
