# Crie um módulo moeda.py => funções: aumentar(), diminuir(), dobro() e metade()
# Importe o módulo e use algumas funções
from aula22_modulos import aumentar, diminuir, dobro, metade

p = float(input('Digite o preço: R$'))
print(f'Aumento em 10%: {aumentar(p,10)}\n'
      f'Decréscimo em 15%: {diminuir(p,15)}\n'
      f'Dobro: {dobro(p)}\n'
      f'Metade: {metade(p)}')
