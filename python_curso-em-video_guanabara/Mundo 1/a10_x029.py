# LEIA: velocidade de um carro
# VERIFICAR: se acima do limite de 80km/h
# RETORNE: multa $7.00/km acima do limite

vel = int(input('Digite a velocidade (km/h): '))
lim = int(80)
mlt = float(7.00)
if vel > lim:
    print('Você estava {}km/h acima do limite de {}km/h. A multa é de R${}.'.format(vel-lim, lim, (vel - lim) * mlt))
else:
    print('Você esteve dentro do limite de velocidade de {}km/h'.format(lim))
