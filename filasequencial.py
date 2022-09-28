class Filaexception(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Fila:
    def __init__(self):
        self.__dados=[]
    
    def estavazio(self)->bool:
        return len(self.__dados)==0
    
    def tamanho(self)->int:
        return len(self.__dados)

    def inserir(self,dado:any):
        self.__dados.append(dado)
    
    def remover(self):
        if self.estavazio():
            raise Filaexception('A fila está vazia ')
        return self.__dados.pop(0)

    def __str__(self) -> str:
        return self.__dados.__str__()

    def imprimir(self):
        return print(self.__str__())

    def inicio(self):
        if self.estavazio(): # é SELF.ESTAVAZIO() POIS O MÉTODO É DO OBJETO FILA E NAO DE LISTA, ENTAO NAO PODEMOS FZR SELF.__DADOS.ESTAVAZIO().
            raise Filaexception('A fila está vazia ')
        return self.__dados[0]


if __name__=='__main__':
    f=Fila()

    #for i in range(1,6):
     #   f.inserir(i*10)
   # print(f)
    try:
        f.remover()
    except Filaexception as fe:
        print(fe)
   # print(f)
    #f.remover()
    #print(f)