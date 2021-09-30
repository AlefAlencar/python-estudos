# aula 20 - FUNÇÕES pt1
'''

def lin():
    print('-'*30)
# PROGRAMA PRINCIPAL
lin()
print(f'{"CURSO EM VÍDEO":^30}')
lin()
print(f'{"PYTHON":^30}')
lin()
print(f'{"Alef Alencar":^30}')
lin()
'''
'''

def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)

mensagem('TÍTULO')
mensagem(123)
mensagem('Alef Alencar')
'''
'''

def soma(a, b):
    print(f'A = {a}; B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# PRINCIPAL
soma(1, 2)
soma(a=3, b=4)
soma(b=6, a=5)
'''
'''

def contador(* num):
    tam = len(num)
    print(num, f'São {tam} números.')


contador(1, 2, 3)
contador(10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
'''


def dobra(lista):
    i = 0
    while i < len(lista):
        lista[i] *= 2
        i += 1


def soma(* varios):
    s = 0
    for num in varios:
        s += num
    print(f'A soma dos valores dá {s}.')


valores = [1, 2, 3, 4, 5]
dobra(valores)
print(f'O dobro dos valores da lista é {valores}')
soma(1, 2, 3, 4, 5)
