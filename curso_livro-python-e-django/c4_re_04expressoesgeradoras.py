#!/usr/bin/env python3
# src/modelo08.py
class Aluno:
    def __init__(self, codigo=0, nome='', media=0):
        self.codigo = codigo
        self.nome = nome
        self.media = media

    def situacao(self):
        if self.media < 4:
            return 'Reprovado'
        elif self.media < 7:
            return 'Recuperação'
        else:
            return 'Aprovado'
# Implementa a classe exemplo alunos para ser usada como exemplo
# de uso de expressões de geradores. Além das expressões que criam
# os geradores codigos e situacoes, a função zip é um gerador também.


alunos = [Aluno(1, 'Pedro', 8),
          Aluno(2, 'Laura', 9),
          Aluno(3, 'Estudapoco', 5),
          Aluno(4, 'Mataula', 3)]
codigos = (aluno.codigo for aluno in alunos)
print(type(codigos))
# <class 'generator'>
situacoes = (aluno.situacao() for aluno in alunos)
print(type(situacoes))
# <class 'generator'>
resultados = {codigo: situacao for codigo, situacao in zip(codigos, situacoes)}
print(type(resultados))

print(codigos)
print(situacoes)

print(resultados)
# {1: 'Aprovado', 2: 'Aprovado', 3: 'Recuperação', 4: 'Reprovado'}
