

class pilhaexception(Exception): #herança de exception  
    def __init__(self,msg):
        super().__init__(msg)



class pilhasequencial:
    def __init__(self): 
        self.__dados=[]

    def vazia(self) -> bool:
        return len(self.__dados)==0

    def tamanho(self) -> int:
        return len(self.__dados)

    def topo (self):
        if self.vazia():
            raise pilhaexception('A pilha está vazia')
        return self.__dados[0]

    def inserir(self,dado):
        self.__dados.insert(0,dado)

    def remover(self):
        if self.vazia():
            raise pilhaexception('A pilha está vazia')
        return self.__dados.pop(0)

    def __str__(self) -> str:
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())


if __name__=='__main__':
    p=pilhasequencial()
    try:
        p.remover()
    except pilhaexception as pe:
        print(pe)

    print(p)


    