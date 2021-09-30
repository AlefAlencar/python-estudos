from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Devolve o código de duas letras do Pygal para um país, dado o seu nome."""
    for code, name in COUNTRIES.items():
        if country_name == name:
            return code
    # Se o país não foi encontrado, devolde None
    return None
