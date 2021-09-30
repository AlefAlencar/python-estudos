# LEIA: comprimento de 3 segmentos de retas
# VERIFIQUE se podem formar um triângulo
# RETORNE: sim ou não

print('Digite o comprimento de 3 segmentos de reta e descubra se é possível formar um triângulo')
sa = (input('Segmento a: '))
sb = float(input('Segmento b: '))
sc = float(input('Segmento c: '))

seg = [sa, sb, sc]
seg.sort()
if seg[0] + seg[1] > seg[2]:
    print('Com os segmentos {} é possível formar um triângulo.'.format(seg))
else:
    print('Com os segmentos {} não é possível formar um triângulo'.format(seg))
