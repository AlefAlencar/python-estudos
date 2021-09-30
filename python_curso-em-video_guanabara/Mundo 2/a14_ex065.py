# MAIOR E MENOR VALORES
# LEIA: vários números inteiros
# RETORNE: média de todos, o maior, e o menor valores lidos.
# O programa deve PERGUNTAR se o usuário quer ou não continuar a digitar valores.
num = soma = media = cont = maior = menor = 0
resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('CONTINUAR? [S/N] ')).upper()
media = soma / cont
print('MÉDIA: {} | MAIOR: {} | MENOR: {}'.format(media, maior, menor))
