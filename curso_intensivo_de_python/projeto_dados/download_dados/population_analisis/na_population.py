import pygal_maps_world.maps as pmw

mapa = pmw.World()
mapa.title = 'Populations of Countries in North America'
mapa.add('North America', {'ca': 3412600, 'us': 309249000, 'mx': 113423000})

mapa.render_to_file('na_population.svg')
