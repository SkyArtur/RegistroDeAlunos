import logging

from colorama import init, Fore, Style


init(autoreset=True)


class ColorFormatter(logging.Formatter):
    LEVEL_COLORS = {
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT,
        'INFO': Fore.GREEN,
        'DEBUG': Fore.CYAN
    }

    def format(self, record):
        color = self.LEVEL_COLORS.get(record.levelname, "")
        text = super().format(record)
        return f"{color}{text}{Style.RESET_ALL}"


class SafeExtraFormatter(logging.Formatter):
    def format(self, record):
        if not hasattr(record, 'detalhe'):
            record.detalhe = ""
        return super().format(record)