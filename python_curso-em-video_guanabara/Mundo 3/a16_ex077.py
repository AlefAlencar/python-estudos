# CRIE TUPLA com várias palavras (não use acentos)
# MOSTRE: as vogais de cada palavra
tupla = ('Programacao', 'Dinheiro', 'Bovespa', 'Milhao')
print('PALAVRA: VOGAIS\n')
for elemento in tupla:
    print(f'{elemento.upper()}: ', end='')
    c = 0
    for letra in elemento:
        if letra in 'aeiou':
            print(letra, end=' ')
    # while c != len(elemento):
    #    if elemento[c] in 'aeiou':
    #        print(elemento[c], end=' ')
        c += 1
    print('\n')
print('FIM')
