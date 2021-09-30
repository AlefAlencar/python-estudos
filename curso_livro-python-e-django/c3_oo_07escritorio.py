#!/usr/bin/env python3
# src/modelo09.py

# O exemplo mostra uma das utilizações da técnica de MÉTODOS PRIVADOS para proteger a
# implementação de um método que será sobrescrito através da herança.

class Material:
    def __init__(self, historico):
        self.historico = []
        self.__atualiza(historico)

    def atualiza(self, historico):
        for historia in historico:
            self.historico.append(historia)
    __atualiza = atualiza


class Escritorio(Material):
    def atualiza(self, mapa):
        for item in mapa.items():
            self.historico.append(item)


martelo = Material(['compra', 'uso', 'concerto'])
print(martelo.historico)  # ['compra', 'uso', 'concerto']
cartucho = Escritorio(['compra', 'descarte'])
hist = cartucho.historico
print(sorted(hist) == ['compra', 'descarte'])  # True
cartucho.atualiza({'recarga': 5, 'nivel': 2})
hist = cartucho.historico
print(sorted(hist, key=str))  # [('nivel', 2), ('recarga', 5), 'compra', 'descarte']
