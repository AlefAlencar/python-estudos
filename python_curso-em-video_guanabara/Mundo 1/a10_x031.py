# LEIA distância de viagem (km)
# VERIFIQUE se <200km, então R$0,50/Km, senão R$0,45/Km
# RETORNE o preço total da passagem

d = int(input('Qual a distância de sua viagem? (Km): '))
t1 = 0.50
t2 = 0.45
if d <= 200:
    tar = t1
else:
    tar = t2
print('O valor total de sua viagem será de R${:.2f}'.format(d*tar))