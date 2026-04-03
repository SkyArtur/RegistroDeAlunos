import logging


class LevelFilter(logging.Filter):

    def __init__(self, *, only=None, min_level=None, max_level=None):
        super().__init__()
        self.only = only
        self.min_level = min_level
        self.max_level = max_level

    def filter(self, record):
        if self.only is not None:
            return record.levelno == self.only
        if self.min_level is not None and record.levelno < self.min_level:
            return False
        if self.max_level is not None and record.levelno > self.max_level:
            return False
        return True