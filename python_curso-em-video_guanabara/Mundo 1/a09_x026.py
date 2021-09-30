# LEIA: frase.
# RETORNE: vezes aparece 'A';
# posição da primeira 'A';
# posição da última 'A'.

frase = str(input('Digite uma frase: ')).upper().strip()
print(frase)
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A posição da primeira letra A é {}'.format(frase.find('A')+1))
print('A posição da última letra A é {}'.format(frase.rfind('A')+1))