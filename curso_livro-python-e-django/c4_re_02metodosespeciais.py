#!/usr/bin/env python3
# src/modelo04.py
class StringInteiro(str):
    def __new__(cls, str_inteiro):
        valor = int(str_inteiro)
        return super(StringInteiro, cls).__new__(cls, str_inteiro)

    def __init__(self, str_inteiro):
        return super(StringInteiro, self).__init__()

    def __repr__(self):
        return '{}({})'.format('StringInteiro', self)

    def __str__(self):
        return self

    def __lt__(self, other):
        return int(self) < int(other)

    def __add__(self, other):
        return str(int(self) + int(other))


string_dez = StringInteiro('10')
string_dois = StringInteiro('2')
print(repr(string_dez))  # StringInteiro(10)
teste = eval(repr(string_dez))
print(teste)  # 10
print(string_dez)  # 10
print(string_dez < string_dois)  # False
print('10' < '2')  # True
print(10 < 2)  # False
print(string_dez + string_dois)  # 12
