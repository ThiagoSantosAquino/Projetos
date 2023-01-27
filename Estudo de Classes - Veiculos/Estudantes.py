#OOP para criação de estudantes como objetos para programação
class Estudantes:
    # contruir o método construtor para os paramentros dos estudantes
    def __init__(self,nome,rg,pai,mae,idade,série,turma,turno,disc,un1,un2,un3):
        self.nome = nome 
        self.rg = rg
        self.pai = pai
        self.mae = mae
        self.idade = 0
        self.série = série
        self.turma = -
        self.tuuno = turno
        self.disciplina = disc
        self.un1 = 0
        self.un2 = 0
        self.un3 = 0
    
    def media(self,un1,un2,un3)
        mf:float= (self.un1+self.un2+self.un3)/3
        print(f"A média final das unidades é {mf}")
        if mf>=5:
            print("Aluno aprovador!!!")
        else:
            print("Aluno em recuperação!!!!")


