"""
Do canal gringo Socratica, alguns exemplos de:

FUNÇÕES ANÔNIMAS/EXPRESSÕES LAMBDA
"""

'''# ==========
def f(x):
    return 3*x + 1


print(f(2))
# ==========
print(lambda x: 3*x + 1)

g = lambda x: 3*x + 1  # <-- "PEP: não atribua um expr lambda, use um def"
print(g(2))
# ==========
full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
print(full_name('  alef', 'CAMARGO'))

# ==========**********==========
scifi_authors = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein',
                 'Arthus C. Clarke', 'Frank Herbert', 'Orson Scott Card',
                 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
print(help(scifi_authors.sort))  # <-- puxou um help para lista
scifi_authors.sort(key=lambda name: name.split(' ')[-1].lower())
print(scifi_authors)  # ^^^ ordenou pelo sobrenome *o* :D '''
