from typing import Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass,field
from datetime import date


@dataclass(slots=True, repr=True)
class Pessoa(ABC):
    """Define a estrutura base para pessoas utilizadas no projeto."""

    id: Optional[int]
    nome: str
    sobrenome: str
    nascimento: date
    idade: int = field(default=0, init=False)

    def __post_init__(self):
        if not isinstance(self.nascimento, str):
            self.idade = (date.today() - self.nascimento).days // 365

    @abstractmethod
    def analisar(self) -> tuple:
        """Retorna os dados necessários para análise da entidade.

        Returns:
            Uma tupla com os dados definidos pela implementação concreta.
        """
        pass

    @abstractmethod
    def dados(self) -> tuple:
        """Retorna os dados principais da entidade.

        Returns:
            Uma tupla com os dados relevantes da implementação concreta.
        """
        pass

    @classmethod
    @abstractmethod
    def gerar(cls, *args, **kwargs) -> Pessoa:
        """Cria uma instância concreta da entidade derivada.

        Args:
            *args: Argumentos posicionais necessários para criação do objeto.
            **kwargs: Argumentos nomeados necessários para criação do objeto.

        Returns:
            Uma instância de ``Pessoa`` ou de uma de suas subclasses.
        """
        pass
