from ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')  # (read), lê o Arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')  # (write) cria o Arquivo, (+) se não existir
        a.close()
    except:
        print('Houve ERRO na criação do Arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler Arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:.<30}{dado[1]:.>7} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO na abertura do Arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO no momento de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
