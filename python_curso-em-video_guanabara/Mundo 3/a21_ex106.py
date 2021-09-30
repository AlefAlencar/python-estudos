# use o Interactive Help, receba o comando desejado e retorne
# com cores
c = ('\033[m',        # 0 = sem cores
     '\033[0;30;41m'  # 1 = vermelho
     # ADICIONE várias cores aqui
     )


def ajuda(com):
    titulo(f'Acessando manual do comando... \'{com}\'', 1)
    help(com)


def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0], end='')


# PRINCIPAL
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou biblioteca >>> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!', 1)
