# BOLETIM ESCOLAR com listas compostas
# LEIA nome e duas notas de vários alunos
# MOSTRE um boletim contendo a média de cada aluno
# PERMITA q o usuário possa mostrar as notas de cada aluno individualmente
# boletim[aluno1[nome, notas[n1, n2], média], aluno2[...]]
boletim = []
aluno = []
notas = []
soma = media = verAluno = 0
resp = ' '
while True:  # entrada de dados (aluno por aluno)
    aluno.append(str(input('Nome: ')).strip())
    for n in range(0, 2):
        notas.append(float(input(f'Nota {n+1}: ')))
        soma += notas[n]
    media = soma / len(notas)
    # armazenamento dos dados
    aluno.append(notas[:])
    aluno.append(media)
    boletim.append(aluno[:])
    # limpeza
    notas.clear()
    aluno.clear()
    soma = media = 0
    # ?continuar?
    while resp not in 'SN':
        resp = str(input('ADICIONAR NOVO? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    resp = ' '
# imprimir boletim (nome e média)
print(f'{"ID":<5}{"NOME":<15}{"MÉDIA":>5}')
for n, a in enumerate(boletim):
    print(f'{n:<5}{a[0]:<15}{a[2]:>5}')
# ?Ver notas de aluno?
while True:
    verAluno = int(input('Digite o [ID] para ver boletim completo (999 para SAIR): '))
    if verAluno == 999:
        break
    print(f'ALUNO: {boletim[verAluno][0]}\n'
          f'1ª nota: {boletim[verAluno][1][0]}\n'
          f'2ª nota: {boletim[verAluno][1][1]}\n'
          f'Média: {boletim[verAluno][2]}')
print("FIM")
