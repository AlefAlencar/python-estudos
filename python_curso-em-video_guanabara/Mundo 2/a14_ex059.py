# CRIANDO UM MENU DE OPÇÕES
# LEIA: dois valores
# MOSTRE menu:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# EXECUTE a opção escolhida

print('MENU DE OPÇÕES')
n1 = 0
n2 = 0
opcao = 0
resultado = 0
while opcao != 5:
    if opcao == 4 or opcao == 0:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor:  '))
    else:
        print(resultado)
    opcao = int(input('[1] SOMAR\n'
                      '[2] MULTIPLICAR\n'
                      '[3] qual é o MAIOR\n'
                      '[4] NOVOS NÚMEROS\n'
                      '[5] SAIR DO PROGRAMA\n'
                      '>>> Qual opção? >>>: '))
    if opcao == 1:
        resultado = '{} + {} = {}'.format(n1, n2, n1 + n2)
    elif opcao == 2:
        resultado = '{} * {} = {}'.format(n1, n2, n1 * n2)
    elif opcao == 3:
        if n1 == n2:
            resultado = '{} = {}'.format(n1, n2)
        elif n1 > n2:
            resultado = '{} > {}'.format(n1, n2)
        else:
            resultado = '{} > {}'.format(n2, n1)
    elif not opcao == 4 or opcao == 5:
        resultado = '***OPÇÃO INVÁLIDA***'
print('FIM')
