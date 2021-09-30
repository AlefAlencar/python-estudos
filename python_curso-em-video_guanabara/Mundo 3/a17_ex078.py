# LEIA: 5 valores numéricos e guarde numa lista
# MOSTRE: o maior, o menor e suas respectivas posições na lista
valores = list()
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}º valor: ')))
    if c == 0:
        maior = menor = valores[0]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

posMaior = posMenor = 0
print(f'VALORES: {valores}')
print(f'MAIOR: {maior} na posição(ões): ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}...', end='')
print()
print(f'MENOR: {menor} na posição(ões): ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}...', end='')

print('\nFIM')
