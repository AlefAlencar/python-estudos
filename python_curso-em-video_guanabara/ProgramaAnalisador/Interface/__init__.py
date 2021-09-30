def leia_int(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print(colorir('ERRO: número inteiro válido.', 'vermelho'))
            continue
        else:
            return n


def colorir(mensagem, cor):
    if cor == 'preto':
        return f'\033[30m{mensagem}\033[m'
    elif cor == 'vermelho':
        return f'\033[31m{mensagem}\033[m'
    elif cor == 'verde':
        return f'\033[32m{mensagem}\033[m'
    elif cor == 'amarelo':
        return f'\033[33m{mensagem}\033[m'
    elif cor == 'azul':
        return f'\033[34m{mensagem}\033[m'
    elif cor == 'roxo':
        return f'\033[35m{mensagem}\033[m'
    elif cor == 'aqua':
        return f'\033[36m{mensagem}\033[m'
    elif cor == 'cinza':
        return f'\033[37m{mensagem}\033[m'
    elif cor == 'branco':  # branco
        return f'\033[38m{mensagem}\033[m'


def linha(texto='', posicao='^', carac_padrao='-', tamanho=40,
          linha_superior=False, linha_central=False, linha_inferior=False):
    """
    Imprime linha formatada. Com ou sem texto. Com ou sem linha, inferior, central ou superior.
    Orientação do texto, se houver:
        - '^': centralizado (padrão)
        - '<': à esquerda
        - '>': à direita
    Caractere que formará a linha, por padrão é o '-'.
    :param linha_superior: imprime uma linha "superior" acima do texto principal.
    :param linha_central: imprime uma linha "central", e se houver texto, conforme a posição.
    :param linha_inferior: imprime uma linha "inferior" abaixo do texto principal.
    :param texto: frase desejado na impressão (Padrão = '[vazio]').
    :param posicao: posição do texto na impressão.
    :param carac_padrao: caractere que formará a linha.
    :param tamanho: tamanho da(s) linha(s), em caracteres.
    :return: texto conforme parâmetros passados.
    """
    if linha_superior:
        print(carac_padrao * tamanho)
    if texto == '':
        print(carac_padrao * tamanho)
    else:
        if linha_central:
            print(f'{texto:{carac_padrao}{posicao}{tamanho}}')
        else:
            print(f'{texto:{posicao}{tamanho}}')
    if linha_inferior:
        print(carac_padrao * tamanho)


def menu(lista_opcoes):
    linha('MENU PRINCIPAL', linha_central=True)
    c = 1
    for opcao in lista_opcoes:
        print(f'{colorir(f"[{c}]","preto")} {colorir(opcao,"aqua")}')
        c += 1
    opcao = leia_int(colorir('Sua opção: ', 'verde'))
    return opcao
