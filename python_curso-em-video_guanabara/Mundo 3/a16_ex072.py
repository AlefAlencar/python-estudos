# NÚMERO POR EXTENSO
# CRIE TUPLA COM UMA CONTAGEM POR EXTENSO, DE 0 A 20
# LEIA: número (0 a 20)
# RETORNE: número por extenso
numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = 'S'
while resp == 'S':
    while True:
        num = int(input('Número [0 a 20]: '))
        if 0 <= num <= 20:
            break
    print(numero[num])
    resp = str(input('CONTINUAR [S/N]: ')).strip().upper()[0]
print('FIM')
