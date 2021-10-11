"""
DESAFIOS HACKERRANK
13. Regex and Parsing (expressões regulares e análise)
"""
# Exemplos
import re

'''# group, groups, groupdict
import re
m = re.match(
    r'(\w+)@(\w+)\.(\w+)', 'username@hackerrank.com'
)
print(m.group(0), '\n',  # correspondência inteira
      m.group(1), '\n',  # primeiro subgrupo
      m.group(2), '\n',
      m.group(3), '\n',
      m.group(1, 3))  # tupla de multiplos subgrupos
print(m.groups())  # tupla de todos as correspondências
n = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)',
             'myname@hackerrank.com')
print(n.groupdict())
a = re.finditer(r'\w', 'http://www.hackerrank.com/')
b = list(map(lambda x: x.group(), re.finditer(r'\w', 'http://www.hackerrank.com/')))
print(a, '\n',
      b)'''

s = 'abc123abc456'
f = re.search(r'\d+', s)
a = re.findall(r'\d+', s)
print(a)
# print(a.end(), '\n',
#       a.start())
# '''

# 1/17 Detetc Floating Point Number {1ª 9/18f 0pt}
'''# {1ª 9/18f, 2ª adicionado try float(S)}
import re  # regex, regular expression
for _ in range(int(input())):  # resumido:
    s = input()
    try:  # adicionado a 2ª tentativa
        float(s)
        print(bool(re.match('^[+-]?[0-9]*.[0-9]+$', s)))
    # "inicio"[+-]"nenhum ou 1"[0-9]"nenhum a varios""ponto tem que ter"[0-9]"um a varios""fim"
    except ValueError:
        print(False)  # '''

''' T F T, F T F, T F T
9
-10.10
-6/4
+7.5
+9/1
8.9
6/9
-9.4
-5%5
+4.10
'''

# 2/17 re.split()
'''import re
regex_pattern = r",."	 # Do not delete 'r'. # bem simples
print("\n".join(re.split(regex_pattern, input())))  # '''

# 3/17 group(), groups() & groudict() {1ª: 2/6f 0pt}
# encontre a primeira repeticao consecutiva de um caractere alfanumérico
'''import re
s = input()
m = re.search(r'([a-zA-Z0-9])\1+', s)
print(m.group()[0])  # '''

# 4/17 re.findall() & re.finditer()
'''import re
s = input()
c = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM '
v = 'aeiouAEIOU'
res = re.findall(r'(?<=[%s])([%s]{2,})[%s]' % (c, v, c), s)
# ?<= "precedido"
# {2,} "dois ou mais"
# %
print(res)
if not res:
    print(-1)
else:
    for i in res:  # OUTPUT
        if i:
            print(i)  # '''

# 5/17 re.start() & re.end()
