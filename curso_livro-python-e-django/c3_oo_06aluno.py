#!/usr/bin/env python3
# src/modelo08.py

# MÉTODOS ESTÁTICOS, são instanciados apenas uma vez, para a Classe.

class Aluno:
    def __init__(self, nome):
        self.nome = nome


class Disciplina:
    limite_vagas = 20

    def __init__(self, nome):
        self.nome = nome
        self.total_matriculas = 0
        self.matriculados = []

    def matricular(self, aluno):
        if self.verifica_vagas(self.total_matriculas, self.limite_vagas):
            self.matriculados.append(aluno)
            self.total_matriculas += 1
        else:
            print('Não há mais vagas em: {}'.format(self.nome))

    @staticmethod
    def verifica_vagas(total_matriculas, limite_vagas):
        return limite_vagas > total_matriculas


calculo = Disciplina('Cálculo')
marcelino = Aluno('Marcelino')
calculo.matricular(marcelino)
print(calculo.total_matriculas)
# 1
print(Disciplina.verifica_vagas(20, 20))
# False
