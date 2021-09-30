# VÁRIOS NÚMEROS COM FLAG
# LEIA: vários números inteiros
# Pare apenas com a flag 999
# RETORNE: quantos números digitados, e soma total. Descosidere a flag

soma = qt = 0
while True:
    num = int(input('Número inteiro ([999] Parar): '))
    if num == 999:
        break
    qt += 1
    soma += num
print(f'| Quantidade de números: {qt} | Soma: {soma} |')
