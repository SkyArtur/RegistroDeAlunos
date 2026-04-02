from typing import Optional


class ValidadoresError(Exception):

    def __init__(self,
        *,
        valor: Optional[int | float | str] = None,
        minn: Optional[int | float ] = None,
        maxx: Optional[int | float ] = None, **kwargs):
        self.valor = valor
        self.minn = minn
        self.maxx = maxx
        self.detalhe = self.valor
        self.message = self.get_message()
        super().__init__(self.message)

    def __str__(self):
        return repr(self.message)

    def get_message(self):
        pass


class ValidarDatasError(ValidadoresError):

    def get_message(self):
        return f'Data inválida. '


class ValidarNumerosError(ValidadoresError):

    def get_message(self) -> str:
        return f'Valor não é um número válido '


class ValidarNumerosMaxxError(ValidadoresError):

    def get_message(self) -> str:
        return f'Valor maior que [{self.maxx}] '


class ValidarNumerosMinnError(ValidadoresError):

    def get_message(self) -> str:
        return f"Valor menor que o mínimo [{self.minn}] "