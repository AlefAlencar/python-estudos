# ANALISADOR COMPLETO
# LEIA: nome, idade, sexo de 4 pessoas
# RETORNE: média de idade, nome homem mais velho, quantas mulheres menos de 20 anos
nome = []
idade = []
sexo = []

soma = 0
ivelho = 0
velho = ''
novas = 0

for c in range(0, 4):
    print('--- {}ª PESSOA ---'.format(c + 1))
    nome.append(str(input('Nome: ')))
    idade.append(int(input('Idade: ')))
    sexo.append(str(input('Sexo ([M/F]): ')).upper())

    soma += idade[c]
    if sexo[c] == 'M' and idade[c] > ivelho:
        velho = nome[c]
        ivelho = idade[c]
    if sexo[c] == 'F' and idade[c] < 20:
        novas += 1

print('A média de idade é {:.1f}.'.format(soma / 4))
print('O homem mais velho é o {} e tem {} anos.'.format(velho, ivelho))
print('{} mulher(es) tem menos de 20 anos.'.format(novas))
