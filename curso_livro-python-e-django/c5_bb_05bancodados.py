from datetime import date
from c5_bb_04bancodados import conectar_banco, criar_cursor, criar_tabela_computador, executar_comando


def inserir_registro_computador(cursor, codigo, nome, aquisicao, vida, marca):
    comando = \
        'INSERT INTO computador(' \
        '   codigo, nome, aquisicao, vida, marca' \
        '   ) VALUES (?, ?, ?, ?, ?)'
    parametros = (codigo, nome, aquisicao, vida, marca)
    executar_comando(cursor, comando, parametros)


# CRIAR a tabela
conexao = conectar_banco(':memory:')
cursor = criar_cursor(conexao)
criar_tabela_computador(cursor)

# INSERÇÃO DE DADOS
inserir_registro_computador(cursor, 1, 'Vostro', date(2015, 1, 10), 365, 'Dell')
inserir_registro_computador(cursor, 2, 'Pavilion', date(2015, 1, 10), 365, 'HP')

# CONSULTA DE DADOS
comando_sql = 'SELECT * FROM computador'
registros = executar_comando(cursor, comando_sql)
registro = registros.fetchone()  # "buscar um"
print(registro)  # (1, 'Voastra', '2015-01-10', 365, 'Dell')
registro = registros.fetchone()
print(registro)  # (2, 'Pavilion', '2015-01-10', 365, 'HP')

# ATUALIZAÇÃO de dados
comando_sql = \
            'UPDATE computador ' \
            '   SET vida = ? where codigo = ?'
parametros = (600, 1)
registros = executar_comando(cursor, comando_sql, parametros)
print(registros.rowcount)  # 1
parametros = (400, 2)
registros = executar_comando(cursor, comando_sql, parametros)
print(registros.rowcount)  # 1

# CONSULTA DE DADOS
comando_sql = 'SELECT * FROM computador'
registros = executar_comando(cursor, comando_sql)
for registro in registros.fetchall():  # "buscar tudo"
    print(registro)
# (1, 'Vastra', '2015-01-10', 600, 'dall')
# (2, 'Polvilion', '2015-01-10', 400, 'lp')
