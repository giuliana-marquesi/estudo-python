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

    #não sei se isso cabe aqui
    def readLembrete(self):
        return 'Data: ' + self.__date.strftime("%d/%m/%y") + '\nDescrição: ' + self.__descr

    def updateLembrete(self, date, descr):
        self.__date = date
        self.__descr = descr
