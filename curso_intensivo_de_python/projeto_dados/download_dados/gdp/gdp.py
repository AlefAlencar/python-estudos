import pygal_maps_world.maps as mwm

import consulta
from consulta import Arquivo

nome = 'gdp_current_usdollar.csv'

fonte = Arquivo(nome)  # CRIA INSTÂNCIA
fonte.carregar_arquivo()

# fonte.mostrar_cabecalho()
# fonte.listar_cabecalho()
# fonte.listar_paises_pib()

print(fonte.cabecalho)
print(fonte.paises)
print(fonte.pibs)
fonte.listar_nomes_pib()
fonte.criar_dicio_nome_pib()

nomes_pib = fonte.paises_pibs
print(nomes_pib)
cod_pib = consulta.cria_dicio_codigo_pib(fonte.paises_pibs)
print(cod_pib)
consulta.listar_dicio_codigo_pib(cod_pib)

# CRIA MAPA DE PAÍSES
'''paises = mwm.World()
paises.title = 'PIB em 2020, por País'
paises.add('PIB, em trilhões de US$', cod_pib)

paises.render_to_file('pib_pais_2020.svg')'''

# CRIA MAPA DE CONTINENTES (incompleto)
'''continentes = mwm.SupranationalWorld()
continentes.title = 'PIB em 2020, por Continente'
continentes.add('Asia', [('asia', 1)])
continentes.add('Europe', [('europe', 1)])
continentes.add('Africa', [('africa', 1)])
continentes.add('North america', [('north_america', consulta.converter_para_trilhao(nomes_pib['North America']))])
continentes.add('South america', [('south_america', consulta.converter_para_trilhao(
    nomes_pib['Latin America & Caribbean']))])
continentes.add('Oceania', [('oceania', 1)])
continentes.add('Antartica', [('antartica', 1)])
continentes.render_to_file('pib_continentes_2020.svg')'''
