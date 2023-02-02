import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

porcent = 80                           # Estabelecer percentual de tamanho de tela

entrada = Tk()                          # Iniciar a criação de tela
entrada.resizable(False,False)
entrada.title("Cadastro de Clientes Pousasda Guaibim")

altura=entrada.winfo_screenheight()     # Capturar as informações de dimensão de altura da tela
largura=entrada.winfo_screenwidth()     # Capturar as informações de dimensão de largura de tela

dim_alt= int(altura*(porcent/100))      # Calculando o percentual da altura com o dado coletado
dim_larg= int(largura*(porcent/100))    # Calculando o percentual da largura com o dado coletado

dimensao=(f"{dim_larg}x{dim_alt}")      # Escrevendo a string que sera usado no modulo geormtry
entrada.geometry(dimensao)              # Definindo a geometria da tela

entrada=ttk.Frame(entrada, relief="sunken")
entrada.grid()

NomeLb = Label(entrada, text="Nome completo do hospede:", background="silver").grid(row=1,column=0)
entNome = Entry(entrada, width=100).grid(row=1,column=1, columnspan=3)

profLb = Label(entrada, text="Profissão:").grid(row=1,column=4, )
entProf = Entry(entrada, width=30).grid(row=1,column=5)

cpfLb = Label(entrada, text="Digite o CPF do responsável:", background="silver").grid(row=2,column=0)
entCpf = Entry(entrada,width=30).grid(row=2,column=1)

nascLb = Label(entrada, text="Data de Nascimento 'ddmmaaaa'").grid(row=2, column=2)
entNasc = Entry(entrada, width=30).grid(row=2, column=3)

endLb = Label(entrada, text="Endereço residencial:").grid(row=3,column=0)
entEnd = Entry(entrada,width=120).grid(row=3, column=1, columnspan=4)

telLb = Label(entrada, text="Telefone para contato:").grid(row=4,column=0)
entTel = Entry(entrada).grid(row=4,column=1)




entrada = mainloop()                    # Manter a tela em loop
