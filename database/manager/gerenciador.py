from __future__ import annotations

from database.connector import Conector
from core import caminho_database

class GerenciadorDatabase:

    def __init__(self, query: str = '', dados: tuple = (), *, debug: bool = False) -> None:
        self.query = query
        self.dados = dados
        self.__arquivo = caminho_database(debug=debug)

    def __enter__(self) -> GerenciadorDatabase:
        self.conn = Conector(arquivo=self.__arquivo)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()
        return

    def create(self) -> None:
        self.cursor.execute(self.query, self.dados)

    def fetch(self, one: bool = False) -> tuple | list[tuple] | None:
        self.cursor.execute(self.query, self.dados)
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def alter(self) -> int | None:
        self.cursor.execute(self.query, self.dados)
        return self.cursor.lastrowid
