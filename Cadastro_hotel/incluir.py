import sqlite3 as sq
from strings import *


def incluir():
    conn = sq.connect("hospedes.db")
    cur = conn.cursor()

    cur.execute(sqltring[1])
    opcao = 'S'

    while opcao.upper() == 'S':
        cpf = input("Digite o número do seu CPF")
        nome = input("Digite o nome do clinete")
        tel = input("Digite o número do telefone com DDD")
        email = input("Digite um email para contanto")
        prof = input("Digite o sua profissão")
        end = input("Digite o seu endereço residencial")
        checkin = input("digite a data de checkin")
        checkout = input("Digite a data de checkout")
        reserva = int(input("Foi feita a reserva? Digite 1 para sim ou 2 para não"))
        reservalor = float(input("Digite o valor creditado para reserva"))
        valordiaria = float(input("Digite o valor da diária"))
        motivo = int(input("Qual o motivo da hospedagem? 1 para profisional ou 2 para lazer"))

        cur.execute(f"string[2]",(cpf,nome,tel,email,prof,end,checkin,checkout,reserva,reservalor,valordiaria,motivo))

        opcao = input("Deseja continuar? (S/N):").upper()
        if opcao != "S":
            break



