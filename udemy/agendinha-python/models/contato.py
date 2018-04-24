import contatoBasico

class Contato(ContadoBasico):
	def __init__(self,dtnasc,nome,idade, telefones):
                ContatoBasico.__init__(self, nome, telefones)
		self.dtnasc = dtnasc
		self.idade = idade

	'''
		implementar getDados e getIdade
	'''
