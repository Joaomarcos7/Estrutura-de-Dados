

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

    def __len__(self)->int:
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
        '''
        s=''
        for i in self.__dados:
            s+=f'{i}'
        return s   ##### MÉTODO RAIZ DE TRANFORMAÇÃO EM STRING,percorre o objeto e concatena cada elemento em uma array
        '''
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())

    def concatena(self,outrapilha:any):
        #Inverter a pilha "outraPilha"
        paux = pilhasequencial()
        while(not outrapilha.estaVazia()):
            paux.inserir( outrapilha.remover())
        # descarregando paux na pilha que recebeu a chamada
        while(not paux.estaVazia()):
            self.inserir( paux.remover())


    def esvazia(self):
        self.__dados.clear()






if __name__=='__main__':


    p=pilhasequencial()
    p.inserir(5)
    try:
        p.remover()
    except pilhaexception as pe:
        print(pe)
    print(len(p))
    