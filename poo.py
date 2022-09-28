from ast import main


class  Ventilador:
    def __init__(self,marca:str,tempo:int):     #T.A.D
            self.__ligado=False
            self.__circulando=False
            self.dados=[marca,tempo]
    def liga(self):
        self.__ligado=True
        print('Ligado')

    def desligado(self):
        self.__ligado=False
        print('Desligado')

    def circular(self):
        self.__circulando=True
        print('Circulando')
    def __str__(self):
        return self.dados.__str__()

if __name__=='__main__':
    arno=Ventilador('arno',3)
    print(arno.dados)