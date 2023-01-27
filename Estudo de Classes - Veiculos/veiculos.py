#OOP - orientação orientada a objetos
class Veiculos:
    #Método construtor (ele constrói o objeto da classe)
    #A palavra self utilizada poderia ser qualquer uma de sua criação, ela é utilzada como uma chave para direcionar os atributos
    #Depois da chave 'self' a resposta dos atributos podem ser digitado aleatoriamente, o 'pot' foi escrito propositalmente fora da ordem para demosntrar isso
    #mas as palavras tem que ser iguais na lista da chave e na resposta do atributo
    # caso não esteja nos parametros as palavras de identificação, como exemplo o ligado, somente a propria classe pode alterar, nenhum externo modifica
    def __init__(self,pot,portas,marca,mod,color,veloc,catmt:bool,marchas:list,vel:float):
        #Atributos Classe/Instância:
        #nesse caso os atributos serão instanciados a método init
        self.qtPortas = portas
        self.marca = marca
        self.modelo = mod
        self.cor = color
        self.potencia = pot
        self.velMaxima = veloc
        self.AtMt = catmt
        self.marchas = [marchas]
        self.ligado = False
        self.velo = vel
        self.__milha = 0
    
    #Getter (Get/obter)
    # @ -> Decorator, simula uma coisa mas não é
    
    
    @property
    def milha(self):
        return self.__milha
    
    #Setter (Set/Atribuir)    
    milha.setter
    def milha(self,valor):
        if valor>0:
            self.velo = valor*1.6
            self.__milha= valor     
    # Método:Ações
    
    def acelerar(self):
        if (self.velo+10)>self.velMaxima:
            print("velocidade máxima atingida!")
            self.velo==self.velMaxima
            
        else:
            for i in range (0,3,3):
                i+=1
                self.velo += 10
    
    def freiar(self):
        if (self.velo-10)<0:
           self.velo==0
           return("O veícuo encontra-se parado!")
            
        else:
            self.velo-=10
            return " "
    
    def ligar(self):
        if self.ligado == True:
            print("Veiculo já está ligado!")
        else:
            print("veiculo ligado!")
            self.ligado =  True 
    
    def desligar(self):
        if not (self.ligado):
            print("Veiculo encontra-se desligado!")
        if self.velo != 0:
                print("Veículo em movimento, não pode ser desligado!")
                print("primeiro pare o veículo")
        else:
            print("Veiculo pode ser desligado!")
            self.ligado = False
            
    #Criar uma ação que vai alterar atributos da classe
    def pintar(self,cor):
        print(f"De {self.cor} para a nova pintura: {cor}")
        self.cor = cor
        
    def inf(self):
        print(f"{self.velo},{self.AtMt},{self.cor},{self.ligado},{self.marca},{self.modelo},{self.potencia}")

    def indicador(self):
        if self.velo == 0:
            print("N")
        else:
            for x in (self.marchas):
                if self.velo<x:
                    print(x)
    
    def velocimetro(self):
        print(self.velo)

    def marchaatual(self):
        if self.ligado:
            if self.velo == 0:
                return "neutro !"
            else:
                for indice,velo in enumerate(self.marchas):
                    if self.velo <= velo:
                        return (indice+1)
        else:
            return "park !"




