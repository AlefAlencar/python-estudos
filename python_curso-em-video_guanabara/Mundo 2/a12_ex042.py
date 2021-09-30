# TIPO DE TRIÂNGULO (Desafio 035)
# LEIA: 3 vértices.
# RETORNE: Tipo de triângulo.
# - Equilátero: todos os lados iguais,
# - Isósceles: dois lados iguais,
# - Escaleno: todos os lados diferentes.

print('TRIÂNGULOS! :D'
      '\nDigite o comprimento dos três segmentos de reta de um triângulo e descubra qual é o tipo:')
s1 = int(input('O primeiro segmento: '))
s2 = int(input('O segundo segmento: '))
s3 = int(input('O terceiro segmento: '))
s = [s1, s2, s3]
s.sort()

if s[0] + s[1] < s[2]:
    print('Não é possível formar um triângulo com essas medidas.')
elif s1 == s2 == s3:
    print('O seu triângulo é Equilátero: todos os lados iguais.')
elif s1 == s2 or s1 == s3 or s2 == s3:
    print('O seu triângulo é Isósceles: dois lados iguais.')
else:
    print('O seu triângulo é Escaleno: todos os lados são diferentes.')
