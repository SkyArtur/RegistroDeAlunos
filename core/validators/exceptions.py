from typing import Optional


class ValidadoresError(Exception):
    """Classe base para erros relacionados aos validadores do projeto."""

    def __init__(self,
        valor: Optional[int | float | str] = None,
        *,
        minn: Optional[int | float ] = None,
        maxx: Optional[int | float ] = None,
        detalhe: str = '', **kwargs):
        """Inicializa a exceção com os dados utilizados na validacao.

        Args:
            valor: Valor associado ao erro de validacao.
            minn: Limite minimo considerado durante a validacao.
            maxx: Limite maximo considerado durante a validacao.
            **kwargs: Argumentos adicionais reservados para extensoes futuras.
        """
        self.valor = valor
        self.minn = minn
        self.maxx = maxx
        self.detalhe = detalhe
        self.message = self.get_message()
        super().__init__(self.message)


    def get_message(self):
        """Retorna a mensagem padrão associada a exceção.

        Returns:
            A mensagem textual correspondente ao erro de validacao.
        """
        raise NotImplementedError('Subclasses de ValidadoresError devem implementar get_message()')


class ValidarDatasError(ValidadoresError):
    """Representa erros de validacao relacionados a datas."""

    def get_message(self):
        """Retorna a mensagem padrão para data invalida.

        Returns:
            A mensagem textual correspondente ao erro identificado.
        """
        return f'Data inválida: {self.valor}'


class ValidarNumerosError(ValidadoresError):
    """Representa erros de validacao relacionados a números inválidos."""

    def get_message(self) -> str:
        """Retorna a mensagem padrão para número invalido.

        Returns:
            A mensagem textual correspondente ao erro identificado.
        """
        return f'Valor [{self.valor}] não é um número válido'


class ValidarNumerosMaxxError(ValidadoresError):
    """Representa erros de validacao para valores acima do limite máximo."""

    def get_message(self) -> str:
        """Retorna a mensagem padrão para valor acima do limite máximo.

        Returns:
            A mensagem textual correspondente ao erro identificado.
        """
        return f'Valor [{self.valor}] maior que o máximo [{self.maxx}]'


class ValidarNumerosMinnError(ValidadoresError):
    """Representa erros de validacao para valores abaixo do limite minimo."""

    def get_message(self) -> str:
        """Retorna a mensagem padrão para valor abaixo do limite minimo.

        Returns:
            A mensagem textual correspondente ao erro identificado.
        """
        return f"Valor [{self.valor}] menor que o mínimo [{self.minn}]"
