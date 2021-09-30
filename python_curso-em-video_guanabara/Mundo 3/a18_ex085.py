# LISTA COM PARES E ÍMPARES
# LEIA 7 números e cadastre em uma única lista e mantenha separados os pares dos ímpares
# MOSTRE os pares e ímpares em ordem crescente
pares = []
impares = []
numeros = [pares, impares]
num = 0
for i in range(0, 7):
    num = int(input(f'{i+1}º valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'PARES: {sorted(pares)}\n'
      f'ÍMPARES: {sorted(impares)}\n'
      f'FIM')
