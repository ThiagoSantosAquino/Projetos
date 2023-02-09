import sqlite3 as sql
from sqlstrings import *

def excluir():
    
    conn  = sql.connect("Produtos.db")
    while True:
        id = int(input("Qual o código do produto que deseja excluir? "))
        cur = conn.cursor()
        cur.execute(sqlStrings[1])
        listaCodigos = cur.fetchall()
        lista=[]
        for item in listaCodigos:
            lista.append(item[0])
        if id in lista: 
            excluir = input("Tem certeza? (s/n)")
            if excluir == 's':
                cur.execute(sqlStrings [2], (id,))
                conn.commit()
                opcao = input("Excluir outro? (s/n)")
                if opcao != 's':
                    break
        else:  
            print("Código inválido")
            break
    
