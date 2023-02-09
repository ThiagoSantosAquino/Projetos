import sqlite3 as sql
from sqlstrings import *

def alterarDesc  ():
    pass
def alterarQt():
    pass
def alterarPeso():
    pass
def alterarVencto():
    pass

def alterarPreco():
    conn = sql.connect("Produtos.db")
    while True:
        codigo = int( input("Código do Produto: ") )
        novoPreco = float( input("Digite o Novo Preço: ") )
        # O Cursor é um MiddleWare entre a Consulta
        #  SQL e o Banco de Dados.
        cur = conn.cursor()
        cur.execute(sqlStrings[1])
        
        listaCodigos = cur.fetchall()
        lista=[]
        for i in range(50):
            print('*', end='')
        
        
        for item in listaCodigos:
            lista.append(item[0])
        
        if codigo in lista:      
            cur.execute(sqlStrings[6], (novoPreco, codigo) )
            conn.commit()
            opcao=input("Alterar outro ? (S/N)")
        
        if opcao != 'S':
            break
        
        else:
            print("Código inválido!")
            break