#
# ! HÁ PACOTES CRIADOS QUE FAZEM PARTE DESSA AULA

from aula22_modulos import numeros

num = int(input('Digite um valor: '))
print(f'O fatorial de {num} é {numeros.fatorial(num)}\n'
      f'O dobro,{numeros.dobro(num)}\nO triplo, {numeros.triplo(num)}')
