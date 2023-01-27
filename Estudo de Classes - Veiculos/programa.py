# Do arquivo veiculos importar a classe Veiculos
from veiculos import Veiculos
from motocicletas import motos
opala = Veiculos("225 CV",5,"Chevrollet","Diplomata","Preto","190 Km/h",False,5,vel=0)
#chamando o método da classe que foi direcionada ao opala, usa o operador ponto '.'
opala.ligar()
#para executar um atributo direcionado ao objeto usamos o operador ponto 
print(opala.cor)

opala.desligar()
opala.desligar()
opala.inf()
opala.pintar("prata")
opala.inf()


#criar outro objeto, partindo da classe motocicleta que herdou a classe veiculos
cg125 = motos(25, 0, "honda", "CG125", "preto", 0, False,[0, 20, 40, 60, 90], 140)
cg125.inf()
cg125.ligar()
cg125.desligar()
cg125.desligar()
cg125.pintar("prata")
cg125.freiar()

#É possivel digitar os paramentros dos atributos fora de ordem, mas precisa identificar.
fazer = motos(marca="yamaha", color="azul", veloc= 150, catmt= False, pot= 21, portas=0, mod="250cc",vel=0 , marchas=[0, 20, 60, 90, 110])
fazer.inf()
fazer.ligar()
fazer.pintar("prata")
fazer.empinar()
fazer.acelerar()
fazer.inf()
print(fazer.freiar())