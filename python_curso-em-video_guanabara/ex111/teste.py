# CRIE pacote com dois módulos
# módulo moeda() e dado()
# Transfira todas as funções
from ex111.utilidadesCeV import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 10)
