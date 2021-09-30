# CRIE um dicionário que ontenha três rios importantes e o país que cada rio corta.
# Exibir frase: 'O [rio] corre o [país]'
# Use um laço para exibir o nome de cada rio no dicionário
# Use um laço para exibir o nome de cada país no dicionário

rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'mississipi': 'estados unidos',
    'dnieper': 'ucrania',
    'elba': 'alemanha',
    'volga': 'russia',
    'ganges': 'india',
    'yangtze': 'china'
}
for rio, pais in rios.items():
    print(f'O rio {rio.title()} corre o {pais.title()}.')

for rio in rios.keys():
    print(f'Rio {rio.title()}')

for pais in rios.values():
    print(f'{pais.title()}')
