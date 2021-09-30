n1 = int(input('Primeiro fator: '))
n2 = int(input('Segundo fator: '))
p = n1 ** n2  # Potenciação
m = n1 * n2  # Multiplicação
d = n1 / n2  # Divisão
di = n1 // n2  # Inteiro da Divisão
dr = n1 % n2  # Resto da Divisão
so = n1 + n2  # Soma
su = n1 - n2  # Subtração
print(
    'Potenciação = {}, Multiplicação = {};'
    '\nDivisão: {:.3f}, Divisão inteiro: {}, Divisão resto: {}; '
    '\nSoma:{}, e Subtração: {}.'.format(p, m, d, di, dr, so, su), end=' ')
print('='*20)

print('{}: O número anterior é {}, e o sucessor é {}.'.format(n1, n1 - 1, n1 + 1))  # desafio05
print('O seu dobro é {}, o triplo, {}, e a raiz quadrada, {}'.format(n1 * 2, n1 * 3, n1 ** (1 / 2)))  # desafio06
print('A média de {} e {} é {:.2f}'.format(n1, n2, (n1 + n2) / 2))  # desafio07
print('{} metros equivale a {} centímetros, ou {} milímetros.'.format(n1, n1 * 100, n1 * 1000))  # desafio08
print(
    'Sendo {} a altura, e {} a largura de uma parede, em metros, equivaleria a uma área de {} metros quadrados'.format(
        n1, n2, n1 * n2))  # desafio11
print('Seria necessário {:.1f} litros de tinta para pintá-la (2m^2 / l)'.format((n1 * n2) / 2))  # desafio11
# desafio09: tabuada
print('Com R${}, você teria US${:.2f}'.format(n1, n1 / 5.50))  # desafio10
print('Sendo R${} o preço de um produto, e {}% o desconto, o valor final será de R${:.2f}'.format(n1, n2,
                                                                                              n1 - (n1 * 5 / 100)))
print('Sendo R${} o sálario do funcionário, se der 15% de aumento, o novo salário será de R${:.2f}'.format(n1 * n2, (
        n1 * n2) * 1.15))
print('{}ºCelsius corresponde a {}ºFarenheit'.format(n1, ((9*n1)/5)+32))
