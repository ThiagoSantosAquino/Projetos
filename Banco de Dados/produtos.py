# Importa a biblioteca do Banco de Dados do SQlite3
import sqlite3 as sq

# Criar uma conexão com o Banco de dados e cria o banco se não existir.
conn = sq.connect ("Produtos.db")
print (conn)

# O cursor é um MiddleWare entre a Consulta
#SQL e o Banco de Dados.
cur = conn.cursor()


cur.execute("""
            CREATE TABLE IF NOT EXISTS Produtos   (
            codigo integer PRIMARY KEY AUTOINCREMENT,
            descricao text,
            preco real,
            qt integer,
            peso real,
            vencimento text )
            """)


# Inserindo dados na tabela do Banco de dados
print("Deseja cadastrar algum produto? (Y/N)?") # UMA PERGUNTA APENAS DE BOAS VINDAS
resp = input().upper() 



#tentando usar while para cadastrar vário produtos

while resp == "Y":
    #criando as variaveis para inserir na tabela
    descricao = input("Digte a descrição do produto: ")
    preco = float(input("Digite o preço: "))
    quant = int(input("Digite a Quantidade em unidades:"))
    massa = float(input("Digite o valor do peso do produto: "))
    vencto = input("Digite a data do vencimento (AAAAMMDD) : ")
    
    # Inserindo na tabela
    cur.execute("""
            INSERT INTO Produtos (
            descricao,
            preco,
            qt,
            peso,
            vencimento
            )
            VALUES(?,?,?,?,?) 
           """, ( descricao,preco,quant,massa,vencto)
           ) # Numa doc String como no exemplo acima as variavéis são chamadas em um tupla fora da doc string e representadas com interrogações 
            # como se fosse um coringa. Eles organizam na ordem em que foi escrita.

    #Salvar ps dados no banco de dados no repositório local
    conn.commit()

    print("Deseja cadastrar mais algum produto? (Y/N)?")
    resp = input().upper()

print("Dados Cadastrados")

cur.execute("""DELETE FROM Produtos WHERE codigo=2""")
conn.commit()