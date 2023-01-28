#Importando a biblioteca TKINTER
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

app = Tk() #Instância do objeto Widget 'Master Window'

app.geometry("800x600")#Função que determina o tamanho da tela que está sendo produzinda
app.resizable(False,False)#impede que o usuario altere manualmente o tamanho da tela utilizando a cursor/seta
app.title("Estoque Versão 1.0")#Função ou método que define o tituo da tela

#Colocando componetes ou Widgets
texto1 = Label(app, text="Digite o nome do cliente: ", background="silver").pack()
#poderia também colocar texto1.pack() em outra linha, mas como é a mesma função, colocamos na sequencia
#o pack é utilizado para organizar a posição na tela, de frma automatica, mas é recomendado usar o 'grid'
'''app, text e beckgroud são parametros da função 'Label' que foi atribuida ao widget texto1,
onde 'app' é o endereço de tela que vai aparecer e deve sempre ser identificado o endereçamento da janela, 'text' é a caixa de texto que vai aparecer e background 
define uma cor de fundo para o texto.
'''
def salvar():
    #O messagebox é uma caixa de mensagem em box opções predefinidas de butões, aqui temos sim ou não
    op = messagebox.askquestion(
        title="Título da Mensagem1",
        message="Quer continuar?"
    )
    
    print(op)
    
def salvar2():
    #O messagebox é uma caixa de mensagem em box opções predefinidas de butões, aqui temos sim, não ou cancelar
    op = messagebox.askyesnocancel(
        title="Título da Mensagem1",
        message="Quer continuar?"
    )
    
    print(op)
    
caixaTxt = Entry(app).pack()#criada uma caixa de texto para inserir os dados que o usuario vai escrever
caixaTxt2 = ttk.Entry(app).pack()#Caixa de texto criado peo metodo ttK, tem uma aprencia diferente

salvar = Button(app, command=salvar, text="SALVAR").pack()#criado um botão para o usuário clicar e executar uma função
#O command direciona qual função vai ser executada ao clicar neste botão
salvar2 = ttk.Button(app, command=salvar2, text="salvar").pack()#botão crado pelo modo ttk

#Agora vamos criar botões de check, ou confirmação, pode ser usado para marcar varias opções e é organizando sua posição usando o método 'place' ao invés de 'pack'
chkbtn1 = StringVar()
cb1 = Checkbutton(app, text = "Checkbutton1", variable = chkbtn1).place(x=10, y=540)

chkbtn2 = StringVar()
cb2 = Checkbutton(app, text = "Checkbutton2", variable = chkbtn1).place(x=10, y=560)

#agora vamos criar o widgetr radiobutton, a diferença para o checkbutton é que ele deve ser utilizado para apenas uma opção.
radio1 = Radiobutton(app, text = "Opção 1"). place(x=10, y=300)
radio2 = Radiobutton(app, text = "Opção").place(x=10, y=320)

app.mainloop()#Método que deixa o objeto da tela em principal em 'loop'e deve ser o último a ser usado