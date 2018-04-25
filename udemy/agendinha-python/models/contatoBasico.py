from telefone import Telefone

class ContatoBasico:

    def __init__(self, nome=' '):
        self.nome = nome
        self._telefones = []

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def addToTelefones(self, telefone):
        self._telefones.append(telefone)

    def getDados(self):
        dados = self.__nome + '\n'

        for telefone in self._telefones:
            dados += telefone.getTelefone() + '\n'

        return dados
