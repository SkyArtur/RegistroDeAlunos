from __future__ import annotations

from datetime import date
from typing import Optional

from .boletim import Boletim
from .pessoa import Pessoa

class Aluno(Pessoa):
    """Representa um aluno com dados pessoais e boletim opcional."""

    def __init__(self, _id: int | None, nome: str, sobrenome: str, nascimento: date, *, boletim: Optional[Boletim] = None, **kwargs):
        """Inicializa uma instância de aluno.

        Args:
            _id: Identificador do aluno.
            nome: Nome do aluno.
            sobrenome: Sobrenome do aluno.
            nascimento: Data de nascimento do aluno.
            boletim: Boletim acadêmico associado ao aluno.
            **kwargs: Argumentos adicionais reservados para extensões futuras.
        """
        super().__init__(_id, nome, sobrenome, nascimento)
        self.boletim = boletim

    def analisar(self) -> tuple:
        """Retorna os dados utilizados na análise básica do aluno.

        Returns:
            Uma tupla com nome, sobrenome e data de nascimento do aluno.
        """
        return self.nome, self.sobrenome, self.nascimento

    def dados(self):
        """Retorna os dados principais de identificação do aluno.

        Returns:
            Uma tupla com identificador, nome, sobrenome e data de nascimento.
        """
        return self.id, self.nome, self.sobrenome, self.nascimento

    @classmethod
    def gerar(cls, _id, nome: str, sobrenome: str, nascimento: date, **kwargs) -> Aluno:
        """Cria uma nova instância de aluno a partir dos dados informados.

        Args:
            _id: Identificador do aluno.
            nome: Nome do aluno.
            sobrenome: Sobrenome do aluno.
            nascimento: Data de nascimento do aluno.
            **kwargs: Argumentos adicionais utilizados na criação do objeto.

        Returns:
            A instância de ``Aluno`` criada com os dados fornecidos.
        """
        return cls(_id, nome, sobrenome, nascimento, **kwargs)
