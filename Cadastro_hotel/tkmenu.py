import tkinter as tk
from tkinter import *
from tkinter import ttk


percent = 80 # definindo o percentual do tamanhho da tela

menu = Tk() #Criando a janela do menu
larguramenu = menu.winfo_screenwidth() #chamando o método para coletar as dimensão da largura da tela windos 
alturamenu = menu.winfo_screenheight() #chamando o método para coletar a dimensão da altura da tela windos

valorDimenslarg = int(larguramenu*(percent/100)) #cálculo do percentual de largura
valorDimensaltu = int(alturamenu*(percent/100)) # cálulo do percentual de altura
menu.geometry(f"{valorDimenslarg}x{valorDimensaltu}") #dimensionando o tamanho da janela

menu.title("Cadastro de clientes Pousada Guaibim") #Definindo o nome da janela menu

# Colocando os componentes no menu, chamados de WINDGETS

textonome = Label(menu,text = "DIGITE O NOME COMPLETO DO CLIENTE:").pack() # texto para o campo de preenchimento nome
caixanome = Entry(menu, background="silver").pack(ipadx=50)

textocpf = Label(menu, text = "DIGITE O NÚMERO DO CPF:").pack() # texto para campo de preenchimento do cpf
caixacpf = Entry(menu, background="silver").pack()

textotel = Label(menu, text = "DIGITE O NÚMERO DO TELEFONE COM DDD:").pack() # texto para preencher o campo de contato
caixatel = Entry(menu, background="silver").pack()

textoemail = Label(menu, text="DiGITE SEU EMAIL PARA CONTATO:").pack() # texto para cadastro do email
caixaemail = Entry(menu, background="silver").pack()

textoprof = Label(menu, text= "QUAL A PROFISSÃO INFORMADA PELO CLIENTE?").pack() # texto para cadastro da profissão
caixaprof = Entry(menu, background="silver").pack()

textoend = Label(menu, text= "CADASTRE O ENDERENÇO DE RESIDÊNCIA DO CLIENTE:").pack() # texto para cadastro de endereço
caixaend = Entry(menu, background="silver").pack()

textomotivo = Label(menu,text= "A HOSPEDAGEM ACONTECEU POR MOTIVO DE TRABALHO OU LAZER?").pack() #Texto para cadastro de motivação de hospedagem
radiomotivoP = Radiobutton(menu, text = "ATIVIDADE PROFISSIONAL",indicator=0).pack()
radiomotivoL = Radiobutton(menu, text= "ATIVIDADE DE LAZER OU VIAGEM",indicator=0).pack()

textoreserv = Label(menu, text="FEZ RESERVA?").pack()
radioreservy = Radiobutton(menu, text="SIM").pack()
radioreservn = Radiobutton(menu, text="NÃO").pack()

textovaloreserv = Label(menu, text="QUAL O VALOR DE PAGAMENTO PELA RESERVA?").pack()
caixareserv = Entry(menu, background="silver").pack()

textovalordiaria = Label(menu, text="VALOR DA DIÁRIA:").pack()
caixavalordiária = Entry(menu,background="silver").pack()

textocheckin = Label(menu,text="DIGITE A DATA DE CHECKIN:").pack() #Texto para informar data de enstrada na hospedagem
caixarcheckin = Entry(menu, background="silver").pack()

textocheckout = Label(menu,text="DIGITE A DATA DE CHECKOUT:").pack()#Texto para cadastrar data de saída do cliente
caixacheckout = Entry(menu,background="silver").pack()













menu.mainloop() #Manter a janela criada aberta em loop, até que seja fechada




