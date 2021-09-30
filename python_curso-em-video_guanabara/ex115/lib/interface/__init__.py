# CRIE um pequeno _sistema modularizado_ para CADASTRAR nome e idade em um ARQUIVO DE TEXTO SIMPLES
# Duas opções: CADASTRAR nova pessoa, LISTAR todas cadastradas
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: digite número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def linha(c='-', tam=42):
    """
    Traça uma linha conforme os parâmetros.
    :param c: caractere que formará a linha
    :param tam: tamanho da linha, em caracteres
    :return: linha (c * tam)
    """
    return c * tam


def cabecalho(txt, tam=42):
    print(linha(tam=tam))
    print(txt.center(tam))
    print(linha(tam=tam))


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc
