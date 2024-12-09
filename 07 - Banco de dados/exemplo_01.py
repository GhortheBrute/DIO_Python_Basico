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

def inserir_mais_registros(conexao, cursor, nome, email):
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



atualizar_registro(conexao, cur, "Giovanna", "giovanna@gmail.com",5)