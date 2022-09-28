from pydoc import doc
from pilhasequencial import pilhaexception

class No:
    def __init__(self,carga:any):
        self.carga=carga   # ATENÇÃO,POIS OS ATRIBUTOS DE NÓ NAO DEVEM SER ENCAPSULADOS AFIM DE SERES USADOS FORA DA SUA CLASSE
        self.prox=None
    def __str__(self):
        return str(self.carga)
class pilha:
    def __init__(self):
        self.__start=None
        self.__tamanho=0

    def vazia(self)-> bool:
        return self.__start==None
        
    def tamanho(self)->int:   #como nao é uma lista,então nao podemos usar o método len() para adquirir de forma simples o tamanho
        '''
        cont=0
        cursor=self.__start
        while(cursor!=None):
            cont+=1
            cursor=cursor.prox
        return cont
        '''
        return self.__tamanho
    
    def __len__(self)->int:
        return self.__tamanho

    def elemento (self,posição:int)->any:
        #retorna a carga indicada por posição

        try:
            assert posição >0 and posição <=self.__tamanho
            deslocamento=self.__tamanho - posição
            cont=0
            cursor=self.__start
            while deslocamento>cont:
                cont+=1
                cursor=cursor.prox
            return cursor.carga

        except AssertionError:
            raise pilhaexception(f'Posição inválida para  a pila atual com {self.__tamanho} elementos')

    def busca(self,conteudo:any)->int:
        cursor=self.__start
        cont=0
        while cursor !=None:
            if cursor.carga==conteudo:
                return self.__tamanho-cont #basicamente retornando o deslocamento 
            cont+=1
            cursor=cursor.prox
        raise  pilhaexception(f'Valor {conteudo} não está na pilha')

    def modificar(self,posicao:int,conteudo:any):
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento = self.__tamanho - posicao

            cont = 0
            cursor = self.__start
            while( deslocamento > cont):
                cont += 1
                cursor = cursor.prox

            cursor.carga = conteudo
        except AssertionError:
            raise pilhaexception(f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')


    def empilhar(self,conteudo:any):
        novo=No(conteudo)
        novo.prox=self.start
        self.start=novo
        tamanho+=1
        

    def desempilha(self)->any:
        #passa pro nó de baixo, transformando-o no topo e retorna o elemento do topo anterior 
        carga = self.__start.carga
        self.__start = self.__start.prox
        self.__tamanho -= 1
        return carga

    def modificar(self,posicao:int,conteudo:any):
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento=self.__tamanho- posicao
            cont=0
            cursor=self.__start
            while deslocamento >cont:
                cont+=1
                cursor=cursor.prox
            cursor.carga=conteudo
        except AssertionError as ae:
            print(ae)

    def busca(self,conteudo:any):
        cursor=self.start
        cont=0
        while cursor != None:
            if cursor.carga==conteudo:
                return self.__tamanho - cont
            cont+=1
            cursor=cursor.prox
        raise  pilhaexception(f'Valor {conteudo} não está na pilha')

    
            





    