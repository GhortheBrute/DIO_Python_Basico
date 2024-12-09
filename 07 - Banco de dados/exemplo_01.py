import sqlite3

conexao = sqlite3.connect('meu_banco_de_dados.db')
cur = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute(
        'CREATE TABLE clientes(id  INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))'
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = ("Jesus", "jes@gmail.com")
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?,?);", data
    )
    conexao.commit()

def inserir_muitos(conexao, cursor, nome, email):
    data = (
        {"nome": "Carvalho", "email": "carv@gmail.com"},
        {"nome": "Fortran", "email": "fort@gmail.com"},
        {"nome": "Python", "email": "pyth@gmail.com"},
        {"nome": "Go", "email": "gogo@gmail.com"},
    )
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES(:nome, :email)", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


def deletar_registro(conexao, cursor, id):
    cursor.execute("DELETE FROM clientes WHERE id=?;", (id,))
    conexao.commit()


def selecionar_unico_registro(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    registro = cursor.fetchone()
    print(registro)


def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome ASC")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)


# atualizar_registro(conexao, cur, "Giovanna", "giovanna@gmail.com",5)
# deletar_registro(conexao, cur, 5 )
#selecionar_unico_registro(conexao, cur, 3)
listar_clientes(cur)
