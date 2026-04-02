from typing import Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass,field
from datetime import date


@dataclass(slots=True, repr=True)
class Pessoa(ABC):
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
        pass

    @abstractmethod
    def dados(self) -> tuple:
        pass

    @classmethod
    @abstractmethod
    def gerar(cls, *args, **kwargs) -> Pessoa:
        pass