#!/usr/bin/env python3
# src/modelo04.py

# MÉTODOS, são instanciados para cada novo objeto instanciado da Classe

class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.livros = []

    def empresta_livro(self, livro):
        self.livros.append(livro)


# Aluno matriculado na instituição de ensino.
# A classe aluno representa um aluno da instituição de ensino.
print(type(Aluno.empresta_livro))  # <class 'function'> | função da classe 'Aluno'
jorge = Aluno(12345, 'Jorge da Capadócia')
print(type(jorge.empresta_livro))  # <class 'method'>   | método, pois já instanciou o objeto 'jorge'
Aluno.empresta_livro(jorge, 'Matemática essencial')   # (self=jorge, livro='texto') !!!
print(jorge.livros)  # ['Matemática essencial']
jorge.empresta_livro('Pedagogia do ensino primário')  # <- SINTÁXE SIMPLIFICADA, 'self' é passado implicitamente
print(jorge.livros)  # ['Matemática essencial', 'Pedagogia do ensino primário']
