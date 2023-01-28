''' 
    Jogo de luta baseado em turnos (modo texto)
    1) Crie uma pasta
    2) Abra o VS Code
    3) Abrir pasta
    4) Crie um arquivo 'jogo.py' 
    Vamos lá!

'''

# Etapa 1: Jgos trabalham dentro de um loop infinito

'''
exemplos de repetições com contagem!
x=int
x=0
while x<10:
    print("loop infinito")
    print(x)
    x+=1
print("fim da execução")


for i in range(10):
    print(f"{i}) infinity school")'''

#com 'and' 99 condiões verdadeiras e uma única falsa, o resultadoé 'falso'.
#com 'or' 99 confições falsas e uma única verdadeira, o resultado é 'verdadeiro'.

#importar módulo externo para o python
# o 'as' é utilizado para associar um nome à biblioteca
from Placar import Placar

import random as rd
lifeBem:int = 10 #para usar a caixa alta na criação do nome da variável, a notação do camelo (Camel Case) é utilizada
LifeMal:int = 10 #para usar a caixa alta nas iniciais, como no exemplo, a notação é o (Pascal Case)
qtdf:int = 2

while lifeBem>0 and LifeMal>0:
    #placar
    Placar(lifeBem, LifeMal)
    #nicia uma variável aleatória com 0 ou 1
    inicio=rd.randint(0,1)
    #0 -> Bem
    #1 -> Mal
    potencia=rd.randint(0,3)
    defe=rd.randint(0,3)
    
    if inicio==0:
        print("O Bem ataca")
        # Usa-se o 'f' para interpolar string com outras variáveis
        print(f" Bem atacou com força {potencia}!!")
        #subtrair a vida do inimigo de acordo co a 'potencia'
        if qtdf != 0 and potencia>=defe:
            resp=input("O Mal defendeu o ataque? (S/N)?")
            if resp=='S':
                qtdf -= 1
                print(f"O mal se defendeu com {defe}")
                potencia=potencia-defe
        else:
            print()
        LifeMal-= potencia
    else:
        print("O Mal ataca")
        print(f"O mal atacou com força {potencia}!!")
        if qtdf != 0 and potencia>=defe:
            resp=input("O bem defendeu o ataque? (S/N)?")
            if resp=='S':
                qtdf -= 1
                print(f"O bem defendeu com {defe}")
                potencia=potencia-defe
        else:
            print()
        lifeBem-= potencia
        
    
    #gera uma pausa cpm o input
    pausa=input('')
    
    
print("infinity School, game over!")