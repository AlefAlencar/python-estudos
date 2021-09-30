# leia 4 nomes de alunos
# retorne 1 nome sorteado
from random import choice
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))

print('O aluno sorteado foi o {}.'.format(choice([n1, n2, n3, n4])))