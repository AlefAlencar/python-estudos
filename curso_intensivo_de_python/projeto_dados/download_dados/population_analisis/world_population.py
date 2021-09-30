import json
import pygal_maps_world.maps as pymaps

from country_codes import get_country_code

# Carrega on dados em uma lista
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Exibe a população de cada país em 2010
'''for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(f'{code}: {population}')
        else:
            print(f'ERROR - {country_name}')'''

# Contrói um dicionário com dados das populações
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

# Agrupa os países em três níveis populacionais
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# Cria o mapa
mapa = pymaps.World()
mapa.title = 'World Population in 2010, by Country'
mapa.add('0-10m', cc_pops_1)
mapa.add('10m-1bn', cc_pops_2)
mapa.add('>1bn', cc_pops_3)

mapa.render_to_file('world_populations.svg')
