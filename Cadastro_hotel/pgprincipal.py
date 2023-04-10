import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela=Tk() # Criando a janela princial do programa de cadastro.

janela.geometry("300x500")  # Definindo os parametros de dimensão da janela princial

janela.resizable(False,False)   # Impedindo que o usuário mova através das setas o tamanho da janela principal

janela.title("GESTÃO HOTELEIRA POUSADA GUAIBIM") # Definido o titulo da tela

#____________ Colocando so componentes Widgets____________

txt1 = Label(janela, text="ESCOLHA A OPÇÃO DESEJADA!").pack()



janela.mainloop()   # Mantendo a janela aberta em loop depois de aberta
