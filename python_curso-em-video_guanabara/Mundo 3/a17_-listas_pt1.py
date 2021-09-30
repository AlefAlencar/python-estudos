# LISTAS parte 1
num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
print(sorted(num))
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0)
print(num)
num.pop(2)
print(num)
num.remove(2)
print(num)
if 1 in num:
    num.remove(1)
    print(num)
else:
    print('Não achei o 4')
''''''
valores = []
for v in valores:
    print(f'{v}...', end='')
print('\n')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

valor = list()
for cont in range(0, 5):
    valor.append(int(input('Digite um valor: ')))
for c, v in enumerate(valor):
    print(f'Posição: {c}, valor:{v}')

a = [2, 4, 6, 8]
b = a  # CRIA UMA LIGAÇÃO
b[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b = a[:]  # COPIA TODOS OS ELEMENTOS DA LISTA
b[2] = 7
print(f'Lista A: {a}')
print(f'Lista B: {b}')
