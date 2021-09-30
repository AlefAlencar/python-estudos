# TABUADA v.2.0
# LEIA: número
# RETORNE: tabuada do número do usuário

n = int(input('Digite o número: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))
