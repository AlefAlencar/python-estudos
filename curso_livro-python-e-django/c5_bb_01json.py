#!/usr/bin/env python3
# src/modelo05.py
"""
API de CEPs.
https://viacep.com.br/ws/04538133/json/
https://viacep.com.br/ws/22220000/json/
"""
import json

ceps = {"google_sp": {
    "cep": "04538-133",
    "logradouro": "Avenida Brigadeiro Faria Lima",
    "complemento": "de 3253 ao fim - lado ímpar",
    "bairro": "Itaim Bibi",
    "localidade": "São Paulo",
    "uf": "SP",
    "ibge": "3550308",
    "gia": "1004"
    }}
msf_brasil = {
    "cep": "22220-000",
    "logradouro": "Rua do Catete",
    "complemento": "até 195/196",
    "bairro": "Catete",
    "localidade": "Rio de Janeiro",
    "uf": "RJ",
    "ibge": "3304557",
    "gia": ""
    }


# O termo serializar é usado para o ato de salvar objetos em arquivos
# de uma forma que possibilite a obtenção desses objetos novamente.
def serializa(ceps_json):
    with open('local.json', 'w') as arquivo:
        json.dump(ceps_json, arquivo)


# Ao deserializar um objeto, ele volta a ficar
# disponível e pode ser manipulado em um programa.
def deserializa():
    with open('local.json') as arquivo:
        return json.load(arquivo)


google_sp = json.dumps(ceps['google_sp'])
print(google_sp)
# '{...}'
serializa(ceps)
novo_ceps = deserializa()
print('msf_brasil' in novo_ceps)
# False
ceps['msf_brasil'] = msf_brasil
serializa(ceps)
novo_ceps = deserializa()
print(novo_ceps['msf_brasil']['logradouro'])
# Rua do Catete
print(novo_ceps['msf_brasil']['bairro'])
# Catete
print(novo_ceps['msf_brasil']['localidade'])
# Rio de Janeiro
print(novo_ceps['msf_brasil']['uf'])
# RJ
print(novo_ceps['msf_brasil']['complemento'])
# até 195/196
