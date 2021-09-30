# MAIOR E MENOR DA SEQUÊNCIA
# LEIA: peso de 5 pessoas
# RETORNE: o maior e o menor peso
maior = 0
menor = 0
for c in range(0, 5):
    peso = int(input('Digite o peso da {}ª pessoa (Kg): '.format(c + 1)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    '''if peso > maior:
        maior = peso
    if menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso'''
print('O maior peso é {}Kg. O menor, {}Kg.'.format(maior, menor))