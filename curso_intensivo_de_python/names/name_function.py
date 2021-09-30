def get_formatted_name(first, last, middle=''):
    """Gera um nome completo formatado de modo elegante.
    >>> get_formatted_name('Alef', 'Camargo')
    'Alef Camargo'
    >>> get_formatted_name('Alef','Camargo', 'Alencar de')
    'Alef Alencar De Camargo'
    """
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()
