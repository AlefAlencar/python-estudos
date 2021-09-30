# FUNCAO notas()
# LEIA notas de vários alunos
# RETORNE um dicionário: quantidade, a maior, a menor, a média da turma, a situação(opcional)
# Adicione a docstring da função
# (..., situacao=True) "ruim, razoavel, boa, excelente"
def turma(*nota, situacao=False):
    """
    --> Função para analisar notas e situação de vários alunos.
    :param nota: float. Nota do aluno.
    :param situacao: bool. Situação da turma com base na média da turma.
    :return:
    """
    dados = {'Quantidade': len(nota),
             'Maior': max(nota),
             'Menor': min(nota),
             'Média': sum(nota) / len(nota)}
    if situacao:
        if dados['Média'] >= 9.0:
            dados['Situacao'] = 'Excelente'
        elif dados['Média'] >= 7.0:
            dados['Situacao'] = 'Boa'
        elif dados['Média'] >= 5.0:
            dados['Situacao'] = 'Razoável'
        else:
            dados['Situacao'] = 'Péssima'
    return f'{dados}'


print(turma(10, 10, 7.5, 9, 8.5, situacao=True))
print(turma(8, 7, 7.5, 6, 8, situacao=True))
print(turma(5, 4.5, 7, 4, situacao=True))
print(turma(2, 3, situacao=True))
print(turma(10, 7, 8))
help(turma)
