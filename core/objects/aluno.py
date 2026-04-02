from datetime import date
from typing import Optional

from .boletim import Boletim
from .pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, _id: int | None, nome: str, sobrenome: str, nascimento: date, *, boletim: Optional[Boletim] = None, **kwargs):
        super().__init__(_id, nome, sobrenome, nascimento)
        self.boletim = boletim

    def analisar(self) -> tuple:
        return self.nome, self.sobrenome, self.nascimento

    def dados(self):
        return self.id, self.nome, self.sobrenome, self.nascimento

    @classmethod
    def gerar(cls, _id, nome: str, sobrenome: str, nascimento: date, **kwargs):
        return cls(_id, nome, sobrenome, nascimento, **kwargs)