# CRIE pacote com dois módulos
# módulo moeda() e dado()
# Transfira todas as funções
from ex112.utilidadesCeV import moeda, dado

p = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 10)
