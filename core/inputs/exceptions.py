

class EntradaTentativasError(Exception):
    def __init__(self, func_name):
        self.detalhe = func_name
        self.message = "Foi excedida o número máximo de chamadas recursivas"
        super().__init__(self.message)
