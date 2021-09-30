'''favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'john': 'python',
    'paul': 'c',
    'george': 'pyhton',
    'lucas': 'VB',
    'chris': 'c',
    'joe': 'ruby',
    'julius': 'python',
}
friends = ['phil', 'sarah', 'chris', 'kisha', 'katherine', 'helen']

# percorrer todas as chaves e valores
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
# percorrer todas as chaves
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f'\t"Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!"')
# percorrer todos os valores
print('\nThe following languages have been mentioned:')
for language in favorite_languages.values():
    print(f'- {language.title()}')
# conjuntos, cada valor sem repetições
print('\nConjuntos (set): sem repetições')
for language in set(favorite_languages.values()):
    print(language.title())
# exercício 6.6 Enquete
print('6.6 - ENQUETE')
for name in favorite_languages:
    if name in friends:
        print(f'Thank you {name.title()} for taking the poll!')
    elif name not in friends:
        print(f'\tHi {name.title()}, could you take my poll, please?')
'''


'''favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are:")
    for language in languages:
        print(language.title())'''

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
