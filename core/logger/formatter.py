import logging

from colorama import init, Fore, Style


init(autoreset=True)


class ColorFormatter(logging.Formatter):
    """Aplica cores às mensagens de log conforme o nível de severidade."""

    LEVEL_COLORS = {
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT,
        'INFO': Fore.GREEN,
        'DEBUG': Fore.CYAN
    }

    def format(self, record):
        """Formata o registro de log com a cor correspondente ao nível informado.

        Args:
            record: Registro de log a ser formatado.

        Returns:
            A mensagem formatada com a cor associada ao nível do log.
        """
        color = self.LEVEL_COLORS.get(record.levelname, "")
        text = super().format(record)
        return f"{color}{text}{Style.RESET_ALL}"


class SafeExtraFormatter(logging.Formatter):
    """Assegura a presença de campos extras esperados durante a formatação."""

    def format(self, record):
        """Formata o registro de log garantindo atributos extras padrão.

        Args:
            record: Registro de log a ser formatado.

        Returns:
            A mensagem formatada com os atributos adicionais necessários.
        """
        if not hasattr(record, 'detalhe'):
            record.detalhe = ""
        return super().format(record)
