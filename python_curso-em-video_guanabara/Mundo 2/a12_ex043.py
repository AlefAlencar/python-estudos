# ÍNDICE DE MASSA CORPORAL (IMC)
# LEIA: peso.
# RETORNE: Nível
# <18.5: Abaixo do peso,
# 18.5 - 25.0: Peso ideal,
# 25.0 - 30.0: Sobrepeso,
# 30.0 - 40.0: Obesidade,
# >40.0: Obesidade mórbida.
# fórmula: peso / (altura x altura)

print('ÍNDICE DE MASSA CORPORAL')
peso = int(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

print('O seu IMC é de {:.1f}, o que indica: '.format(imc))
if imc < 18.5:
    print('Abaixo do peso :/.')
elif imc < 25.0:
    print('Peso ideal. :)')
elif imc < 30.0:
    print('Sobrepeso. :|')
elif imc < 40.0:
    print('Obesidade. :o')
else:
    print('Obesidade mórbida. :O')