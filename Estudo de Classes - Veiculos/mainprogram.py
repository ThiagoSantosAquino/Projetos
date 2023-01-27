# Do arquivo veiculos importar a classe Veiculos
from veiculos import Veiculos


opala = Veiculos("225CV",5,"chevrolet","Diplomata","preto",230,False,[40,70,120,180,230],0)
#chamando o método da classe que foi direcionada ao opala, usa o operador ponto '.'
opala.ligar()
#para executar um atributo direcionado ao objeto usamos o operador ponto 
print(opala.cor)

for x in range(9):
    opala.acelerar()
    opala.velocimetro()
    
opala.marchaatual()

opala.pintar("prata")

opala.inf()
opala.desligar()
opala.inf()






''' lista como usar e como chamar
lista=["joão", "maria", "carla"]
for posição, elemente(lista)
    print(posição+1,elementos)'''

Pajero=Veiculos("150CV","5 portas","MitSubish","Sport hpe","Prata",160,True,"4 marchas")