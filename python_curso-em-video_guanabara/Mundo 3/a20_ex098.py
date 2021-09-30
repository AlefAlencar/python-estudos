# FUNÇÃO contador() recebe: início, fim, passo
# REALIZE 3 contagens:  1 a 10 (+1), 10 a 0 (-2), personalizado
# = 1 2 3 4 5 6 7 8 9 10
# = 10 8 6 4 2 0
# = personalizado, de frente pra trás e vice-versa, negativos também
# se passo=0 => 1
from time import sleep


def contador(i, f, p):
    if p == 0:  # se for zero
        p = 1
    if i > f:  # para incluir o último termo
        f -= 1
    else:
        f += 1
    if i > f and p > 0:  # para calcular com núm negativo
        p *= -1
    for n in range(i, f, p):  # CÁLCULO
        print(n, end=' ')
        sleep(0.2)
    print(f'FIM!\n{"-"*30}')


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Digite o início: ')),
         int(input('Digite o fim:    ')),
         int(input('Digite o passo:  ')))

print('<<<<< ENCERRADO >>>>>')
