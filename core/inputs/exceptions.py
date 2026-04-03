

class EntradaTentativasError(Exception):
    def __init__(self, detalhe):
        self.detalhe = detalhe
        self.message = f"Função <{detalhe}> excedeu o número máximo de chamadas"
        super().__init__(self.message)
