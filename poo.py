class  Ventilador:
    def __init__(self):     #T.A.D
            self.__ligado=False
            self.__circulando=False
    def liga(self):
        self.__ligado=True
        print('Ligado')

    def desligado(self):
        self.__ligado=False
        print('Desligado')

    def circular(self):
        self.__circulando=True
        print('Circulando')

