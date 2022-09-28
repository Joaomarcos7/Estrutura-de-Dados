from logging import exception


def __str__(self): # modo de se fazer metodo especial str para qualquer linguagem, tem que transformar str seu objeto para poder printar
    s=''
    for i in self.object:
        s+=f'{i}'
    return s 

def imprimir(self):
    print(self.__str__()) #retorna a impressao da instancia do objeto 






def __str__(self):
    return self.object.__str__() #modo fácil de fazer método espeical str em python, deve-se transformar em objeto para poder printar seu objeto

def imprimir(self):
    print(self.__str__()) #retorna a impressao da instancia do objeto 



def __len__(self):
    return len(self.object)

def tamanho(self):
    return len(self.object)

    #criação de classe de exceção especial 

    class jmexception(exception):
        def __init__(self,msg) -> None:
            super().__init__(msg) #com isso vai dar para dar raise jmexception('mensagem aqui ')


            