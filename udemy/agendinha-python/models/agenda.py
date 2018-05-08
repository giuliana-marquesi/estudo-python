from models.lembrete import Lembrete

class Agenda:
        
	__lembretes = []
	
	def __init__(self, name, owner, typeAgenda):
		self.__name = name
		self.__owner = owner
		self.__typeAgenda = typeAgenda
	
	@property
	def lembretes(self):
		return self.__lembretes
	
	def addLembrete(self, lembrete):
		self.__lembretes.append(lembrete)
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		self.__name = name
	
	@property
	def owner(self):
		return self.__owner
	
	@owner.setter
	def owner(self, owner):
		self.__owner = owner
	
	@property
	def typeAgenda(self):
		return self.__typeAgenda
	
	@typeAgenda.setter
	def typeAgenda(self, typeAgenda):
		self.__typeAgenda = typeAgenda
		
	def read_agenda(self):
		message = 'Agenda: ' + self.__name + ' Dono: ' + self.__owner + ' Tipo: ' + self.__typeAgenda + '\n'
		
		for lembrete in self.__lembretes:
			message += lembrete.read_lembrete() + '\n'
		
		return message
	
	def update_agenda(self, name, owner, typeAgenda):
		self.__name = name
		self.__owner = owner
		self.__typeAgenda = typeAgenda
	

	def delete_all_lembretes(self):
		self.__lembretes.clear()
		
	def delete_lembrete(self, lembrete):
		self.__lembretes.remove(lembrete)
	
	def search_lembrete(self, descr):
                matched_lembretes = []
                for lembrete in self.__lembretes:
                        if descr in lembrete.descr:
                                matched_lembretes.append(lembrete)

                return matched_lembretes
