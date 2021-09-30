# AULA 10 CONDIÇÕES PT1
# LEIA: duas notas
# RETORNE: a média;
# mensagem se acima ou abaixo de x.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if(m >= 6.0):
    print('Sua média foi boa! Parabéns')
    print('Você é o máximo!' if m >= 9 else 'O suficiente...')
else:
    print('Sua média foi ruim! Vá estudar mais')
