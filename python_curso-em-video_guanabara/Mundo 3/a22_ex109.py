# APERFEIÇOE o ex_108
# Adicione um parâmetro a mais nas funçoes do ex_107, para retornar o valor formatado ou não.
from aula22_modulos import aumentar, diminuir, dobro, metade, moeda, opcional

p = float(input('Digite o preço: R$'))
print(f'Aumento em 10%: {aumentar(p,10,True)}\n'
      f'Decréscimo em 15%: {diminuir(p,15)}\n'
      f'Dobro: {dobro(p,True)}\n'
      f'Metade: {metade(p)}')
