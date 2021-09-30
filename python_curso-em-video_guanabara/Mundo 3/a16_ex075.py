# LEIA: 4 valores e GUARDE numa TUPLA
# MOSTRE: quantas vezes aparece o valor 9, posição do primeiro 3 digitado, quais os números pares
tupla = (int(input('Digite o 1º/4 valor: ')),
         int(input('Digite o 2º/4 valor: ')),
         int(input('Digite o 3º/4 valor: ')),
         int(input('Digite o 4º/4 valor: ')))
print(f'Tupla toda: {tupla}')
print(f'O 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro 3 digitado está na {tupla.index(3)+1}ª posição.')
else:
    print('O 3 não está na tupla.')
p = 0

print('Números pares na tupla:')
for n in tupla:
    if n % 2 == 0:
        print(n)
        p += 1
if p == 0:
    print('Não há números pares na tupla.')
print('FIM')
