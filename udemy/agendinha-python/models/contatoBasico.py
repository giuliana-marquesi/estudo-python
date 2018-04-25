from telefone import Telefone

class ContatoBasico:

    __telefones = None

    def __init__(self, nome=' '):
        self.nome = nome
        self.__telefones = []

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefones(self):
        return self.__telefones

    @telefones.setter
    def telefones(self, telefone):
        self.__telefones.append(telefone)

    def getDados(self):
        dados = self.__nome + '\n'

        for telefone in self.__telefones:
            dados += telefone.getTelefone() + '\n'

        return dados
