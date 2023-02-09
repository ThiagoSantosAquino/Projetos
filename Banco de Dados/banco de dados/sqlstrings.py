sqlStrings  = {
    1: "SELECT * FROM Produtos",
    2: "DELETE FROM Produtos WHERE codigo = ?",
    3: '''INSERT INTO produtos (
                        descricao,
                        preco,
                        qnt,
                        peso,
                        vencimento
                    )
                    VALUES(?,?,?,?,?)
                ''',
    4:'''
            CREATE TABLE IF NOT EXISTS Produtos (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT,
            preco REAL,
            qnt INTEGER,
            peso REAL,
            vencimento TEXT )
             ''',
    5: "UPTADE Produtos SET descricao = ? WHERE codigo = ?",
    6: "UPTADE Produtos SET preco = ? WHERE codigo = ?",
    7: "UPTADE Produtos SET qnt = ? WHERE codigo = ?",
    8: "UPTADE Produtos SET peso = ? WHERE codigo = ?",
    9: "UPTADE Produtos SET vencimento = ? WHERE codigo = ?"
}