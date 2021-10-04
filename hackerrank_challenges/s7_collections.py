"""
DESAFIOS HACKERRANK

07. Collections
"""
import collections

# Exemplos
'''
# Counter
myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
print(collections.Counter(myList))
collections.Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# .itens(), .keys(), e .values() funcionam com Counter 
# DefaultDict
d = collections.defaultdict(list)
d['a'].append('a1')
d['b'].append('b1')
d['a'].append('a2')
d['b'].append('b2')
d['b'].append('b3')
d['b'].remove('b2')
print(d)
for i in d.items():
    print(i)
# NamedTuple
Point = collections.namedtuple('Point', 'x,y')
pt1 = Point(1, 2)
pt2 = Point(3, 4)
dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
print(Point, pt1, pt2, dot_product)
Car = collections.namedtuple('Car', 'Price Mileage Colour Class')
print(Car)
xyz = Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(xyz, xyz.Price, xyz.Mileage)
ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['b'] = 2
ordinary_dict['c'] = 3
ordered_dict = collections.OrderedDict()
ordered_dict['c'] = 1
ordered_dict['b'] = 2
ordered_dict['a'] = 3
print(ordinary_dict, '\n', ordered_dict)
# '''

# 1/8 Counter (easy)
'''# INPUT
# 1. X numero de calçados;
# 2. lista de tamanhos;
# 3. N clientes;
# 4. de cada cliente, tamanho e preço desejado.
# OUTPUT: Receita ganha por Raghu.

# INPUT
input()
shoe_sizes = collections.Counter(list(map(int, input().split())))
costumers = []
res = 0
for _ in range(int(input())):
    c = list(map(int, input().split()))
    costumers.append(c)
    if shoe_sizes[c[0]] > 0:
        shoe_sizes[c[0]] -= 1
        res += c[1]
    # print(shoe_sizes[c[0]])
# costumers = [c for c in (list(map(int, input().split())) for _ in range(int(input())))]
print(f'{shoe_sizes}\n{costumers}\n$: {res}') 
#print(collections.Counter(shoe_sizes)) '''

# 2/8 DefaultDict (easy)
'''# INPUT
n, m = list(map(int, input().split()))
d = collections.defaultdict(list)
for _ in range(n):
    d['A'].append(input())
for _ in range(m):
    d['B'].append(input())
# OUTPUT
for c in d['B']:
    for i, cc in enumerate(d['A']):
        if cc == c:
            print(i+1, end=' ')
    print(-1) if c not in d['A'] else print()  # if reposicionado, só. '''

# 3/8 NamedTuple (easy)
'''# INPUT tabela
total = 0
n = int(input())  # numero de estudantes
Metadado = collections.namedtuple('aluno', input())  # nomes das colunas, em qualquer ordem
for _ in range(n):
    a = Metadado(*input().split())
    total += int(a.MARKS)
print(Metadado.__doc__)  # ver as 
print(total/n)
# REFATORADO:
total, n, Metadado = 0, int(input()), collections.namedtuple('a', input())
print(sum(int(Metadado(*input().split()).MARKS) for _ in range(n))/n)  # '''

# 4/8 OrderedDict (easy)
'''# od = collections.OrderedDict()
# INPUT
# for _ in range(int(input())):
#     string = input().split()
#     net_price, item_name = int(string.pop(-1)), ' '.join(string)
#     if item_name in od:
#         od[item_name] += int(net_price)
#     else:
#         od[item_name] = int(net_price)
# # OUTPUT
# print(od)
# for item, res in od.items():
#     print(item, res)
# REFATORANDO
od = collections.OrderedDict()
for _ in range(int(input())):
    *item_name, net_price = input().split()
    try:
        od[' '.join(item_name)] += int(net_price)
    except KeyError:
        od[' '.join(item_name)] = int(net_price)
for item, res in od.items():
    print(item, res)  # '''

# 5/8 Word Order (medium)
'''d = collections.OrderedDict()
for _ in range(int(input())):
    i = input()
    try:
        d[i] += 1
    except KeyError:
        d[i] = 1
print(len(d))
for k, v in d.items():
    print(v, end=' ')
print(d)  # '''

# 6/8 deque() (easy)
'''d = collections.deque()
for _ in range(int(input())):
    eval('d.{0}({1})'.format(*input().split()+['']) )
print(d)
for _ in d:
    print(_)  # '''

# 7/8 Piling Up! (medium)
'''for t in range(int(input())):  # INPUT
    _, d = input(), collections.deque(map(int, input().split()))
    # # solucao anterior, 2/6 passed
    # a = max([d[0], d[-1]])
    # print(d, 'max', a)
    # for _ in range(len(d)):
    #     if a >= d[0] >= d[-1]:
    #         a = d.popleft()
    #         print(d, 'popleft', a)
    #     elif a >= d[-1] >= d[0]:
    #         a = d.pop()
    #         print(d, 'pop', a)
    #     else:
    #         print(d, a, 'FALSE')
    #         print('No')
    # else:
    #     print('Yes')
    #     print(d, a, 'TRUE')
    imin, ilen, i = d.index(min(d)), len(d)-1, 0
    while d[i] >= d[i+1] and i+1 <= imin:
        i += 1
        print('ok left')
    while d[ilen] >= d[ilen-1] and imin <= ilen-1:
        ilen -= 1
        print('ok right')
    print('Yes') if i == imin and ilen == imin else print('No')  # '''

# 8/8 Company Logo (medium)
'''# print: primeiros 3 mais repetidos caracteres
# se quantidade iguais: ordem alfabética
s = collections.Counter(sorted(input())).most_common(3)
print(s)
for k, v in s:
    print(k, v)  # '''