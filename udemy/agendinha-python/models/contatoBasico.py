class ContatoBasico:
    def __init__(self, nome=' ', telefones= []):
        self.nome = nome

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @telefones.setter
    def telefones(self, telefone):
        telefones.add(telefone)

    def getDados(self):
        return self.__nome + telefones
