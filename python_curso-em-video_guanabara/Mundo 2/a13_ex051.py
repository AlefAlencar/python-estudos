# PROGRESSÃO ARITMÉTICA
# LEIA: primeiro termo, e razão
# RETORNE: os 10 primeiros termos dessa PA (progressão aritmética)

pt = int(input('PROGRESSÃO ARITMÉTICA.\n Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
print(pt)
t = pt
for c in range(1, 10):
    t += rz
    print(t)
