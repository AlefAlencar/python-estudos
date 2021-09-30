# REESCREVA a função leiaInt() do ex104
# INCLUA a possibilidade da digitação de um número de tipo inválido
# CRIE leiaFloat() com a mesma funcionalidade
def leiaint(n=None):
    while True:
        try:
            n = int(input('Número inteiro: '))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: digite número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return print(f'{n}: inteiro CERTO')


def leiafloat(n=None):
    while True:
        try:
            n = float(input('Número real: '))
        except ValueError:
            print(f'\033[31mERRO: digite número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário não informou dado.\033[m')
            continue
        else:
            return print(f'{n}: real CERTO')


# n = int(input('Inteiro: '))
leiaint()
leiafloat()
