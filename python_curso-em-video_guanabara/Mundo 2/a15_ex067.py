# TABUADA v3.0
# LEIA: número
# RETORNE: tabuada
# Repita o processo
# INTERROMPA quando foi negativo
num = 0
c = 1
print('-'*10, 'TABUADA', '-'*10)
while True:
    num = int(input('Número ([<0] Interromper): '))
    if num < 0:
        break
    while c != 10:
        c += 1
        print(f'{num} x {c} = {num * c}')
    c = 1
print('FIM')
