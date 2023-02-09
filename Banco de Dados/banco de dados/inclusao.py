
import sqlite3 as sq
from sqlstrings import *

def inclusao():
    conn  = sq.connect("Produtos.db")
    cur = conn.cursor()

    cur.execute(sqlStrings[4])
    opcao = 'S'
    while opcao.upper() == 'S':
        descricao = input("Digite a descrição: ")
        preco = float(input("Digite o preço: "))
        qnt = int(input("Digite a quantidade: "))
        peso = float(input("Digite o peso (Kg): "))
        venc = input("Digite a data de vencimento (AAAA/MM/DD): ")

        cur.execute(f"sqlStr[3]", (descricao, preco, qnt, peso, venc))
    
        conn.commit()
        opcao = input("Continuar? (S/N): ").upper()
        if opcao !=  'S':
            break
    
