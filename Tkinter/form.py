from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import *                               # o '*' seria todas as funções da biblioteca
from janelaesc import jan


percentLarg = 80

janela = Tk()                                       # usado para criar a janela. Estanciar um objeto da classe Tk()

alturaTela = janela.winfo_screenheight()            # Chama o método que capta as informações da dimensão da altura de tela do usuário windows
larguraTela = janela.winfo_screenwidth()            # Chama o método que capta as informações da dimensão da largura de tela do usuário windows

valoDimensla=int(larguraTela*(percentLarg/100))     # Calcula o percentual depois de coletar a dimensão de largura da tela
valoDimensal=int(alturaTela*(percentLarg/100))      # Calcula o percentual depois de corletar a dimensao de altura da tela

dimensao = f"{valoDimensla}x{valoDimensal}"         # Cria o valor da dimensão que será jogada no parametro da geometry a seguir! 
janela.geometry(dimensao)                           # Dimensionando o tamanho da janela

frm1 = ttk.Frame(janela,relief="sunken")                # Criando um frame dentro da janela
frm1.grid()

lblNome = Label(frm1, text="Digite o seu nome:").grid(row=1, column=0) 
#frm1.grid(row=1, column=0) também é um método, alternativa à usar o grid no fim do argumento como acima!
# veja o exemplo na criação da caixa de escrita de texto abaixo!
entNome = Entry(frm1)                               #Criando uma caixa de entrada de texto
entNome.grid(row=1, column=1, columnspan=2 )         # Utlizando um grid para organizar onde fica a caixa de entrada de texto
# O parametro columnspan mescla o espaço de duas colunas para organizar a caixa, no exemplo aqui!

lblEnd = Label(frm1, text="Digite seu endereço,").grid(row=3, column=0)
lblEnd = Label(frm1, text="Inclua logradouro:").grid(row=3,column=1)
entEnd = Entry(frm1).grid(row=3, column=2)

def salvar():                                               # Crianda a função salvar e atribuindo ao botão criado
    print("Salvando...")
    #messagebox.showinfo(message="Arquivo salvo!")
    
    jan1 = jan(janela)
    
btnSalvar = Button(frm1, text="Salvar", command=salvar)     # Criando um botaão salvar.
btnSalvar.grid(row=4,column=2)                              #Posicionando utilizando o metodo grid 

janela.mainloop()                                   # Criando a ultima linha para carregar a janela, ele fica no loop para a jenela ficar sempre presente na tela


