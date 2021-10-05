"""
DESAFIOS HACKERRANK

09. Errors and Exceptions
"""

# Exemplos
# Não há

# 1/2 Exceptions (basic)
'''for _ in range(int(input())):
    try:
        a, b = list(map(int, input().split()))
        print(a/b)
    except ValueError as error:
        print('Error Code:', error)
    except ZeroDivisionError as error:
        print('Error Code:', error)
    print(a, b)  # '''

# 2/2 Incorrect Regex (basic)
'''import re
for _ in range(int(input())):
    r = input()
    try:
        re.compile(r)
        print(r, 'True')
    except:
        print(r, 'False')  # '''
