"""
DESAFIOS HACKERRANK
12. Python Functionals
"""


# 1/3 Map and Lambda expression
import math

'''def fibonacci(n):
    fibo = [0, 1]
    for _ in range(13):
        fibo.append(fibo[-2] + fibo[-1])
    return fibo[0:n]

nn = int(input())
print(list(map(lambda x: x**3, fibonacci(nn)))))  # '''


# 2/3 validate list of email adress with filter()  (medium)
'''import re


def fun(s):
    padrao = '^[a-zA-Z0-9_-]+[@][a-zA-Z0-9]+[.]+[a-zA-Z]{2,3}$'
    return re.match(padrao, s)


def filter_mail(emails):
    return list(filter(fun, emails))


emails = []
for _ in range(int(input())):
    emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)  # '''

# 3/3 Reduce() (medium)
'''from fractions import Fraction
from functools import reduce


def product(fracs):
    t = 'complete essa linha com um reduce()'
    return t.numerator, t.denominator


r = lambda x, y: x + y
fracs = []
for _ in range(int(input())):
    fracs.append(Fraction(*map(int, input().split())))
result = product(fracs)
print(*result)  # '''
