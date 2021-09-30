# APERFEIÇOE o ex_107
# Crie uma função moeda para padronizar a exibição monetaria de valores em R$
from aula22_modulos import aumentar, diminuir, dobro, metade, moeda

p = float(input('Digite o preço: R$'))
print(f'Aumento em 10%: {moeda(aumentar(p,10))}\n'
      f'Decréscimo em 15%: {moeda(diminuir(p,15))}\n'
      f'Dobro: {moeda(dobro(p))}\n'
      f'Metade: {moeda(metade(p))}')
