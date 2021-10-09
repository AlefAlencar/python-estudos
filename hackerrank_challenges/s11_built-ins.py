"""
DESAFIOS HACKERRANK
11. Built-ins
"""
# 1/6 Any or All {1ª: 6/7f 16p/20  ?}
'''_, l = input(), list(input().split())
r = True  # 1ª
for x in l:
    if int(x) < 0:
        r = False
    if '5' in x:
        r = x == x[::-1]
print(r)  # 

w = all([int(n) > 0 for n in l])  # resumido
z = any([n == n[::-1] for n in l if '5' in n])  # falha se nao tiver '5' na lista
print(w, z)  # '''

# 2/6 Zipped!
'''marks = []  # notas
st, subjects = list(map(int, input().split()))  # alunos, materias
for _ in range(subjects):
    marks.append(list(map(float, input().split())))
z = list(zip(*marks))
print(z)
for s in z:
    print(f'{sum(s)/subjects:.1f}')  # '''
# 3/6 Input()
'''values = list(map(int, input().split()))
x = values[0]
k = values[1]
print(eval(input()) == k)  # '''

# 4/6 Python Evaluation
'''eval(input())  # '''


# 5/6 Athlet Sort (medium)
'''n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input())

arr.sort(key=lambda x: x[k])
for linha in arr:
    print(linha)  # '''

# 6/6 ginortS1324 = Sorting1234 (medium)
'''s = list(input())
ss = 'Sorting1234'

s.sort()
s.sort(key=lambda l: l.islower())
s.sort(key=lambda l: l.isupper())
s.sort(key=lambda l: l.isnumeric() and int(l) % 2 == 1)
s.sort(key=lambda l: l.isnumeric() and int(l) % 2 == 0)

print(s)  # '''
