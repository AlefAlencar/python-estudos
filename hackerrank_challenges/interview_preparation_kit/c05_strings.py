"""
HACKERRANK prepração para entrevista
05.Strings
"""


def make_anagram(a, b):
    a = sorted(a)
    b = sorted(b)
    c = []
    for v in a:
        try:
            x = b.remove(v)
            c.append(x)
        except ValueError:
            pass
    return a, b, (len(a) - len(c)) + (len(b) - len(c))


a = input()
b = input()
print(make_anagram(a, b))
''' expected: 30
fcrxzwscanmligyxyvym
jxwtrhvujlmrpdoqbisbwhmgpmeoke
'''