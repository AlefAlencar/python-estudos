# GERENCIAMENTO DE ARQUIVO

# VERIFICAR existência
# CRIAR
# LER
# CADASTRAR

def ver_exist_arq(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} CRIADO.')


def ler_arq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo.')
    else:
        print('Leitura funcionando.')
    finally:
        a.close()
