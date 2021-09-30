# CAIXA ELETRÔNICO
# LEIA: valor a sacar
# RETORNE: quantas cédulas de cada valor serão entregues (50, 20, 10, 1)
print('='*10, 'CAIXA ELETRÔNICO', '='*10)
valor = int(input('Quanto deseja sacar? R$'))
total = valor
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'{totalCedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
'''nota50 = nota20 = nota10 = nota01 = 0
saque = int(input('Quanto deseja sacar? R$'))
nota50 = saque // 50
saque -= nota50 * 50
nota20 = saque // 20
saque -= nota20 * 20
nota10 = saque // 10
saque -= nota10 * 10
nota01 = saque
print(f'R$50: {nota50}\nR$20: {nota20}\nR$10: {nota10}\nR$1: {nota01}'''