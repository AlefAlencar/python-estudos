#!/usr/bin/env python3
# src/modelo08.py
import re


def verifica_cep(cep):
    expressao = '\d{5}-\d{3}'
    return re.match(expressao, cep) is not None


def verifica_hora(hora):
    expressao = '([01]\d|2[0-4]):[0-5]\d'
    return re.match(expressao, hora) is not None


def verifica_nome_identificador(identificador):
    expressao = '[a-zA-Z_][a-zA-Z0-9_]*'
    return re.match(expressao, identificador) is not None


print(verifica_cep('80000-123'))  # True
print(verifica_cep('123-123'))  # False
print(verifica_hora('11:02'))  # True
print(verifica_hora('25:03'))  # False
print(verifica_nome_identificador('var5_valida3'))  # True
print(verifica_nome_identificador('2_var_invalida'))  # False
