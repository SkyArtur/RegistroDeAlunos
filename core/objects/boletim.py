from dataclasses import dataclass

@dataclass(eq=True, order=True)
class Nota:
    id: int
    valor: float

@dataclass(init=False)
class Boletim:

    def __init__(self, *args):
        controle = 1
        for valor in args:
            setattr(self, f"n{controle}", valor if isinstance(valor, Nota) else Nota(0, valor))
            controle += 1

    @property
    def notas(self) -> list:
        return [n.valor for n in self.__dict__.values() if n is not None]

    @property
    def media(self) -> float:
        return round(sum(self.notas) / len(self.notas), 2)

    @property
    def situacao(self) -> str:
        situacao = 'Reprovado'
        if self.media >= 7:
            situacao = 'Aprovado'
        elif self.media >= 3:
            situacao = 'Recuperação'
        return situacao