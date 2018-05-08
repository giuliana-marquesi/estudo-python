class Lembrete:
    def __init__(self, date, descr):
        self.date = date
        self.descr = descr

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    
    @property
    def descr(self):
        return self.__descr

    @descr.setter
    def descr(self, descr):
        self.__descr = descr

    def read_lembrete(self):
        return 'Data: ' + self.__date.strftime("%d/%m/%y") + ' Descrição: ' + self.__descr

    def update_lembrete(self, date, descr):
        self.__date = date
        self.__descr = descr
        
