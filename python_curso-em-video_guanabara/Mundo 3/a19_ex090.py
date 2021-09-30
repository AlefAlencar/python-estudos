# DICIONÁRIO EM PYTHON
# LEIA nome e média de um aluno, guarde também a situação (aprov/reprov) em um dicionário
# MOSTRE o conteúdo da estrutura
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] > 7.0:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >5.0:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print(aluno)
for k, v in aluno.items():
    print(f'{k}: {v}')
