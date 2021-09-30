"""
DESAFIOS HACKERRANK

Subdomínios nesse arquivo:
  - Introduction
  - Basic Data Types
  - Strings (exceto o último, "Merge The Tools!")

  ! Apenas a partir do subdomínio 04 Sets ("Conjuntos") que os desafios estão identificados e descritos.

Identificação do desafio:
##### tipo, dificuldade: nome_desafio
    Descrição da solução em comentários.
    Remova as aspas triplas para poder executar o código do desafio específico. Recoloque-as para não executar.
"""


########################################################################################################################
#####
'''x, y, z = 1, 2, 2
n = 3

# res = [[a for a in range] for _ in range(11)]

if x >= 0 and y >= 0 and z >= 0 and n >= 0:
    # sem l.c.
    lista = [list(i for i in range(x+1)), list(j for j in range(y+1)), list(chances for chances in range(z+1))]
    final = []
    parte = []
    for a in lista[0]:
        for b in lista[1]:
            for c in lista[2]:
                parte = [a, b, c]
                if a + b + c != n:
                    final.append(parte)

    # list comprehension
    res = [[f, g, h] for f in range(x+1) for g in range(y+1) for h in range(z+1) if f+g+h != n]

print(res)'''

#####
'''n = int(input())
arr = map(int, input().split())

arr = set(list(arr))
arr.remove(max(arr))
print(max(arr))'''

#####
'''lista = []
for _ in range(int(input())):   #
    name = input()              #
    score = float(input())      #

    lista.append([name, score])

notas = sorted(set([a[1] for a in lista]))

lista_penultimos = [aluno[0] for aluno in lista if len(notas) > 1 and aluno[1] == notas[1]]
lista_penultimos.sort()

# print(lista)
# print(notas)
# print(lista_penultimos)

for a in lista_penultimos:
    print(a)'''

#####
'''# Imprimir a média do nome da consulta
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

notas = student_marks[query_name]
media = 0
for i in notas:
    media += i

media = media/3

print(notas)
print(f'{media:.2f}')'''

#####
'''num = list(map(int, input().split()))

subjects = []

for _ in range(num[1]):
    subjects.append(list(map(float, input().split())))
for n in range(num[0]):
    soma = 0
    for s in subjects:
        soma += s[n]
    print(f'{soma/num[1]:.1f}')

print(num)
print(subjects)
# print(list(zip(s for s in subjects)))'''

#####
'''values = list(map(int, input().split()))
x = values[0]
chances = values[1]
print(eval(input()) == chances)
# >>> 1 4
# >>> x**3 + x**2 + x + 1
# True'''

#####
'''lista = []
# append    # insert    # sort
# pop       # remove    # reverse
# print
for _ in range(int(input())):
    command = input().split()

    if command[0] == 'print':
        print(lista)
    elif len(command) == 1:
        eval(f'lista.{command[0]}()')
    elif len(command) == 2:
        eval(f'lista.{command[0]}({command[1]})')
    else:
        eval(f'lista.{command[0]}({command[1]},{command[1]})')'''

#####
'''n = int(input())
integer_list = map(int, input().split())

tupla = tuple(integer_list)

print(hash(tupla))'''

#####
'''def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line

line = input()
result = split_and_join(line)
print(result)'''

#####
'''def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)'''

#####
'''def count_substring(string, sub_string):
    n = 0
    for a in range(len(string)):
        n += string.count(sub_string, a, a+len(sub_string))
    return n

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)'''

#####
'''s = input()
s = list(s)
an = a = d = lw = up = False
for letra in s:
    an = an or letra.isalnum()
    a = a or letra.isalpha()
    d = d or letra.isdigit()
    lw = lw or letra.islower()
    up = up or letra.isupper()

print(an)
print(a)
print(d)
print(lw)
print(up)'''

#####
'''import textwrap


def wrap(string, max_width):
    string = '\n'.join(textwrap.wrap(string, width=max_width))
    # for i in range(len(string)):
    #   string = string.insert(i, '\n')
    return string


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)'''

#####
'''hw = input().split()
h2 = int(hw[0])//2
w = int(hw[1])
c = '.|.'
for i in range(h2):
    print(f'{c*i}{c}{c*i}'.center(w, '-'))

print('WELCOME'.center(w, '-'))

for i in range(h2, 0, -1):
    print(f'{c*(i-1)}{c}{c*(i-1)}'.center(w, '-'))'''

#####
'''def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        print(f'{i:>{width}} '
              f'{oct(i)[2:]:>{width}} '
              f'{hex(i)[2:].upper():>{width}} '
              f'{bin(i)[2:]:>{width}}')

n = int(input())

print_formatted(n)'''

#####
'''def print_rangoli(size):
    abc = string.ascii_letters[:26]  # 0 Pega o abcdário
    completo = []
    # 1 Desce linha a linha até o centro
    for li in range(size-1, -1, -1):
        print('h', li)
        linha = []
        # 1.1 Cria a primeira metade da linha
        for le in range(size-1, li-1, -1):
            print('i', le)
            linha.append(abc[le])
        # 1.2 Cria a segunda metade (Copia e inverte a primeira)
        sm = linha[:]
        for le in range(len(linha)-2, -1, -1):  # Começa a partir do penúltimo elemento
            linha.append(sm[le])
        # 1.3 Salvar a linha inteira
        completo.append(linha)
        print(linha)
    # 2 Cria a segunda metade do rangoli
    smc = completo[:]
    for li in range(len(completo)-2, -1, -1):
        completo.append(smc[li])
        print(smc[li])
    print(completo)
    for li in completo:
        print('-'.join(li).center((size*4)-3, '-'))
        # tam = size + size-1 + size + size -2

n = int(input())
print_rangoli(n)'''

#####
'''import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(so):
    s2 = []
    so = so.split()
    for w in so:
        s2.append(w.capitalize())
    so = str(' '.join(s2))
    return so


s = input()
result = solve(s)

print(result)'''

#####
'''# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# Prints| string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
def minion_game(palavra):
    # print(palavra)  #
    palavra = palavra.upper()
    vogais = 'AEIOU'
    cont_cons = cont_vog = 0
    for i, letra in enumerate(palavra):
        print('Letra:', letra)
        if letra in vogais:
            cont_vog += len(palavra) - i
            print("Vogais:", cont_vog)
        else:
            cont_cons += len(palavra) - i
            print("Consoantes:", cont_cons)
    if cont_cons > cont_vog:
        print(f'Stuart {cont_cons}')
    elif cont_vog > cont_cons:
        print(f'Kevin {cont_vog}')
    else:
        print('Draw')


s = input()
minion_game(s)'''

# Strings, medium: Merge The Tools!
# string s, integer chances, substring t
# n = len(s)
# len(t) = n/chances, n%chances=0

# u0: t0 = 'AAB' -> u0 = 'AB'
# u1: t1 = 'CAA' -> u1 = 'CA'
# ...


def merge_the_tools(string, k):
    string = list(string)
    for n in range(0, len(string), k):
        u = []
        for c in string[n:n+k]:
            if c not in u:
                u.append(c)
        print(''.join(u))


string, k = input(), int(input())
merge_the_tools(string, k)  # '''
