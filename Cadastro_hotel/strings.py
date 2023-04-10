# Criar um dicionário para usar nos menus

sqltring = {
    1: """ CREATE TABLE IF NOT EXISTIS cadastro(
        cpf INTEGER PRIMARY KEY,
        nome TEXT,
        tel TEXT,
        email TEXT,
        prof TEXT,
        end TEXT,
        checkin DATE,
        chekout DATE,
        reserva INTEGER,
        reservalor REAL,
        valordiaria REAL,
        motivo INTEGER)
    ) """,
    2: """ INSERT INTO cadastro (cpf, nome, tel, email, prof, end, checkin, checkoutm,reserva, reservalor, valordiaria, motivo)VALUES(?,?,?,?,?,?,?,?,?,?,?,?) 
    """,
    3: """SELECT cpf FROM cadastro""",
    4: """ DELETE FROM cadastro WHERE cpf = delcpf""",
    5: """ UPDATE cadastro SET cpf WHERE cpf = conscpf""",
    6: """ UPDATE cadastro SET nome WHERE cpf = conscpf""",
    7: """ UPDATE cadastro SET tel WHERE cpf = conscpf""",
    8: """ UPDATE cadastro SET email WHERE cpf = conscpf""",
    9: """ UPDATE cadastro SET prof WHERE cpf = conscpf""",
    10:""" UPDATE cadastro SET end WHERE cpf = conscpf""",
    11:""" UPDATE cadastro SET checkin WHERE cpf = conscpf""",
    12:""" UPDATE cadastro SET checkout WHERE cpf = conscpf""",
    13:""" UPDATE cadastro SET motivo WHERE cpf = conscpf"""
}

    

