#!/usr/bin/env python3
# src/modelo09.py
from urllib.request import urlopen
from json import loads


def consulta_cep(cep):
    url_template = 'https://viacep.com.br/ws/{cep}/json/'
    url = url_template.format(cep=cep)
    local_json = urlopen(url).read()  # o resultado da consulta
    local_str = local_json.decode()  # o conteúdo obtido é convertido em string
    local = loads(local_str)  # converte para uma estrutura de dados da linguagem Python, no caso um dicionário.
    return local


def formata_cep(local):
    return 'Endereço: {logradouro} - ' \
        'Cidade: {localidade} - ' \
        'Estado: {uf}.'.format(**local)


local = consulta_cep('18155000')
ordenados = [item for item in sorted(local.items())]
filtra_info = [item for item in ordenados if 'info' not in item[0]]
for campo in filtra_info:
    print(campo[0], campo[1])
# bairro Botafogo
# cep 22290-906
# complemento 116
# gia
# ibge 3304557
# localidade Rio de Janeiro
# logradouro Rua Lauro Muller
# uf RJ
print(formata_cep(local))
# Endereço: Rua Lauro Muller, 116 - Cidade: Rio de Janeiro ...
