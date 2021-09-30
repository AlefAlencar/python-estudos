import sqlite3
from datetime import date


def conectar_banco(nome_bd):
    return sqlite3.connect(nome_bd)


def criar_cursor(conexao):
    return conexao.cursor()


def criar_tabela_computador(cursor):
    comando = \
        'CREATE TABLE IF NOT EXISTS' \
        '   computador (' \
        '       codigo INTEGER PRIMARY KEY,' \
        '       nome VARCHAR,' \
        '       aquisicao DATE,' \
        '       vida INTEGER,' \
        '       marca, VARCHAR' \
        '   )'
    executar_comando(cursor, comando)


def executar_comando(cursor, comando, parametros=None):
    if parametros:
        cursor.execute(comando, parametros)
    else:
        cursor.execute(comando)
    return cursor


# PRINCIPAL
conexao = conectar_banco(':memory:')  # criar o banco de dados na memória. Encerrado o programa, o BD deixa de existir.
print(type(conexao))  # <class 'sqlite3.Connection'>
cursor = criar_cursor(conexao)
print(type(cursor))  # <class 'sqlite3.Cursor'>
criar_tabela_computador(cursor)
