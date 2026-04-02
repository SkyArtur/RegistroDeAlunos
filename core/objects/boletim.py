from dataclasses import dataclass

@dataclass(eq=True, order=True)
class Nota:
    """Representa uma nota individual associada a um identificador."""

    id: int
    valor: float

@dataclass(init=False)
class Boletim:
    """Representa o conjunto de notas e o resultado acadêmico de um aluno."""

    def __init__(self, *args):
        """Inicializa o boletim a partir de notas ou valores numéricos.

        Args:
            *args: Valores numéricos ou objetos ``Nota`` utilizados na composição
                do boletim.
        """
        controle = 1
        for valor in args:
            setattr(self, f"n{controle}", valor if isinstance(valor, Nota) else Nota(0, valor))
            controle += 1

    @property
    def notas(self) -> list:
        """Retorna a coleção de valores numéricos registrados no boletim.

        Returns:
            A lista de notas cadastradas no boletim.
        """
        return [n.valor for n in self.__dict__.values() if n is not None]

    @property
    def media(self) -> float:
        """Calcula a média aritmética das notas do boletim.

        Returns:
            A média final arredondada para duas casas decimais.
        """
        return round(sum(self.notas) / len(self.notas), 2)

    @property
    def situacao(self) -> str:
        """Determina a situação acadêmica com base na média final.

        Returns:
            A situação acadêmica correspondente ao desempenho obtido.
        """
        situacao = 'Reprovado'
        if self.media >= 7:
            situacao = 'Aprovado'
        elif self.media >= 3:
            situacao = 'Recuperação'
        return situacao
