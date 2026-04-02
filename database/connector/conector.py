import sqlite3
from pathlib import Path


class Conector:
    __instance = None
    __slots__ = ['conexao']

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Conector, cls).__new__(cls)
        return cls.__instance

    def __init__(self, *, arquivo: Path | str, **kwargs) -> None:
        self.conexao = sqlite3.connect(arquivo)

    def cursor(self) -> sqlite3.Cursor:
        return self.conexao.cursor()

    def commit(self) -> None:
        self.conexao.commit()

    def close(self) -> None:
        self.conexao.close()
