import sqlite3 as sql
from sqlstrings import *

def relatorio():
    conn  = sql.connect("Produtos.db")
    cur = conn.cursor()
    cur.execute(sqlStrings[1])

    lista = cur.fetchall()
#for x in range (5): 
    #print(f"(Produto: {lista[x][1]}, R$ {lista[x][2]})")
    id, d, preco, qnt, peso, venc  = lista[1]
    print(d, preco)
#print(lista{[linha][coluna]})
#a primeira coluna é do codigo