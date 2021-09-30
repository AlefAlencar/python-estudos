#!/usr/bin/env python3
# src/modelo02.py

# PROPRIEDADES, GETTERS, SETTERS
# Criamos as propriedades codigo e vida, que farão a validação no método setter.
# O que acontece na prática em Python é que o método setter é chamado
# quando realizamos uma operação de atribuição (“=”), e o getter é chamado sempre que
# precisamos recuperar o valor do atributo.

class Computador:
    def __init__(self, codigo, nome, aquisicao, vida, marca):
        self._codigo = codigo
        self.nome = nome
        self.aquisicao = aquisicao
        self._vida = vida
        self.marca = marca

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        if codigo > 0:
            self._codigo = codigo
        else:
            raise ValueError('Código precisa ser maior que 0 (zero).')

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, vida):
        if vida < 0:
            raise ValueError('Vida útil não pode ser negativa.')
        else:
            self._vida = vida

    def alerta_manutencao(self):
        # TODO: calcular período de manutenção.
        pass


eicir = Computador(1, 'Eicir Um', '20/10/2013', 600, 'Eicir')
# Comentar a próxima linha para executar o resto do código.
# Descomentar para ver a exceção.
# eicir.codigo = 0
# Traceback (most recent call last):
# ...
# ValueError: Código precisa ser maior que 0 (zero).
# Comentar a próxima linha para executar o resto do código.
# Descomentar para ver a exceção.
# eicir.vida = -10
# Traceback (most recent call last):
# ...
# ValueError: Vida útil não pode ser negativa.
print(eicir.codigo, eicir.vida)
# 1 600
