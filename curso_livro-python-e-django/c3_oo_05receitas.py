#!/usr/bin/env python3
# modelo07.py

# Nesse exemplo vemos o que acontece quando usamos ATRIBUTOS DE CLASSE COM TIPOS MUTÁVEIS.

class Receita:
    etapas = []

    def __init__(self, etapas=None):
        self.etapas.extend(etapas)


class Alimento(Receita):
    def __init__(self, etapas=None):
        super().__init__(etapas)


class Remedio(Receita):
    def __init__(self, etapas=None):
        super().__init__(etapas)


panetone = Alimento(['Assar em forno pré-aquecido'])
melol = Remedio(['Adicionar princípio ativo'])

print(panetone.etapas)
# ['Assar em forno pré-aquecido', 'Adicionar princípio ativo']
print(melol.etapas)
# ['Assar em forno pré-aquecido', 'Adicionar princípio ativo']
print(Receita.etapas)
# ['Assar em forno pré-aquecido', 'Adicionar princípio ativo']

bolo = Alimento(['Cobrir com morangos frescos'])
aipoglos = Remedio(['Centrifugar por 30 minutos'])

print(Receita.etapas)
# ['Assar em forno pré-aquecido', 'Adicionar princípio ativo',
# 'Cobrir com morangos frescos', 'Centrifugar por 30 minutos']
