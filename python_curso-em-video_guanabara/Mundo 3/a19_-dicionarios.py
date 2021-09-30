# AULA 19 - DICIONÁRIOS
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['peso'] = 98.5
print(pessoas.values())

'''brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
print(f'brasil: {brasil}')
brasil.append(estado1)
print(f'brasil: {brasil}')
brasil.append(estado2)
print(f'brasil: {brasil}')
print(brasil[1['sigla']])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    #print(e)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
