#!/usr/bin/env python3
# src/modelo05.py

# Herança, atributos

class Produto:
    def __init__(self, nome, imposto, custo):
        self.nome = nome
        self.imposto = imposto
        self.custo = custo

    def preco(self, quantidade):
        return (self.custo + (self.custo * self.imposto)) * quantidade


class Alimento(Produto):
    def __init__(self, nome, imposto, custo, validade):
        super().__init__(nome, imposto, custo)
        self.validade = validade


class Roupa(Produto):
    def __init__(self, nome, imposto, custo, tamanho):
        super().__init__(nome, imposto, custo)
        self.tamanho = tamanho


bola = Produto('Noique', 0.5, 120.0)
macarrao = Alimento('Espaguete', 0.4, 5.0, 30)
camisa = Roupa('Calvo', 0.45, 30.0, 'G')
print(bola.preco(1))
# 180.0
print(macarrao.preco(2))
# 14.0
print(camisa.preco(1))
# 43.5
