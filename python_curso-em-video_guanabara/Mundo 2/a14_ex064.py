# TRATANDO VÁRIOS VALORES v1.0
# LEIA: vários números inteiros
# PARE quando digitar 999 (flag)
# RETORNE: quantos números digitados e qual foi a soma deles, desconsidere a flag
lista = []

n = cont = soma = 0
n = int(input('Digite: um número (999 para SAIR): '))
while n != 999:
    lista.append(n)
    soma += n
    cont += 1
    n = int(input('Digite: um número (999 para SAIR): '))
print('Você digitou {} números e a soma é {}.'.format(cont, soma))
