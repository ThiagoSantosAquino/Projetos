import sqlite3 as sq                # Importar a biblioteca sqlite3

conn = sq.connect("hospedes.db")    # Estabelece uma conexão com o banco de dados e o cria caso não exista
print(conn)

cur = conn.cursor()                 # o metodo conn.cursor é um Middleware entre o SQL e o Banco criado, uma conexão

cur.execute(""" CREATE TABLE IF NOT EXISTS bancohotel(
            cpf integer PRIMARY KEY,
            nome text,
            Profissão text,
            nascimento integer,
            endereço text,
            telefone text)
            """)


