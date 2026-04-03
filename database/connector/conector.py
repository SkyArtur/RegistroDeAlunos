import sqlite3
from pathlib import Path


class Conector:
    __slots__ = ['conexao']

    def __init__(self, *, arquivo: Path | str) -> None:
        self.conexao = sqlite3.connect(arquivo)

    def cursor(self) -> sqlite3.Cursor:
        return self.conexao.cursor()

    def commit(self) -> None:
        self.conexao.commit()

    def rollback(self) -> None:
        self.conexao.rollback()

    def close(self) -> None:
        self.conexao.close()
