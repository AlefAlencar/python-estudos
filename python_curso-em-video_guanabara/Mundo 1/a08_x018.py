# leia ângulo
# retorne seno cosseno tangente
from math import sin, cos, tan, radians
ang = radians(float(input('Digite o ângulo: ')))
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(sin(ang), cos(ang), tan(ang)))
