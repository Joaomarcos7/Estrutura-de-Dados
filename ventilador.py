ventilador=[False,False]

def liga():
    ventilador[0]=True
    print('Ligado')

def desliga():
    ventilador[0]=False
    print('Desligado')

def circular():
    ventilador[1]=True
    if ventilador[0]==True:
        print('Circulando')
    else:
        print('Não circula')

