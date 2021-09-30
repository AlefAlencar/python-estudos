# FUNÇÃO área() receba dimensões de um terreno retangular (larg x comprim)
# MOSTRE a área do terreno.


def apresentacao(txt):
    print('-'*40)
    print(f'{txt:^40}')
    print('-'*40)


def area(l, c):
    a = l * c
    print(f'A área do terreno é de {a:.2f}m²')


# PRINCIPAL
apresentacao('ÁREA DE TERRENO RETANGULAR')
area(float(input('Informe a largura do terreno: ')),
     float(input('Informe o comprimento do terreno: ')))
