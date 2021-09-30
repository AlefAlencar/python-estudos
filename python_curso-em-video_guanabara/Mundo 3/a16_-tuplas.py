# TUPLAS
# tupla é uma estrutura composta e imutável
# tupla (), lista [], dicionário {}.

lanche = ('burguer', 'suco', 'pizza', 'pudim', 'batata frita')
# FATIAMENTOS, manipular tuplas
print(lanche[1])  # MOSTRA O ELEMENTO 1 suco
print(lanche[0:2])  # MOSTRA OS ELEMENTOS 0 burguer E 1 suco
print(lanche[1:])  # MOSTRA OS ELEMENTOS 1 E SEGUINTES suco, pizza, pudim
print(lanche[-1])  # MOSTRA O ÚLTIMO ELEMENTO: 3 pudim
print(lanche[-2])  # MOSTRA O PENÚLTIMO ELEMENTO: 2 pizza
print(lanche[-3:])  # MOSTRA A PARTIR DO -3 suco ADIANTE -2 pizza e -1 pudim

len(lanche)  # NÚMERO DE ELEMENTOS: 4

print('------ for ------')

# for SE NÃO PRECISAR DA POSIÇÃO
for comida in lanche:
    print(f'Vou comer {comida}')
# CLÁSSICO
for cont in range(0, len(lanche)):
    print(lanche[cont])
# ALÉM DO DADO, ME DÁ A POSIÇÃO
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
#
print(sorted(lanche))  # ORDENAR. NOTE AS chaves [] NO PRINT, OU SEJA, CRIOU E MOSTROU UMA LISTA, JÁ QUE TUPLA É IMUTÁVEL

a = (2, 5, 4)
b = (5, 8, 1, 2)
print(a)
print(b)
c = a + b  # CRIA UMA TUPLA c E JUNTA AS TUPLAS a E b
print(c)
print(c.count(5))  # CONTA QUANTAS VEZES APARECE O TERMO ESPECIFICADO
print(c.index(8))  # MOSTRA A POSIÇÃO DO TERMO ESPECIFICADO
print(c.index(5, 1))  # MOSTRA A POSIÇÃO A PARTIR DE UM PONTO

pessoa = ('Alef', 39, 'M', 56.0)
print(pessoa)  # TUPLA PODE TER DADOS DE TIPOS DIFERENTES
del(pessoa)  # É POSSÍVEL EXCLUIR A TUPLA INTEIRA
