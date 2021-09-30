import pygal_maps_world.maps as pmw

mapa = pmw.World()
mapa.title = 'North, Central, and South America'

mapa.add('North America', ['ca', 'mx', 'us'])
mapa.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
mapa.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

mapa.render_to_file('americas.svg')