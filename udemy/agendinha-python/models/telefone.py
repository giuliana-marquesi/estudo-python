class Telefone:
    def __init__(self,numero,tipo):
        self.numero = numero
        self.tipo = tipo

    def getTelefone(self):
        return str(self.numero) + " " + str(self.tipo)
