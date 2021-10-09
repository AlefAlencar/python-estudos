"""
DESAFIOS HACKERRANK
13. Regex and Parsing (expressões regulares e análise)
"""

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

# 2/17 Re.split()
'''import re
regex_pattern = r",."	 # Do not delete 'r'. # bem simples
print("\n".join(re.split(regex_pattern, input())))  # '''

# 3/17 