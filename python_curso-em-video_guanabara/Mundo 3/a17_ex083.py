# LEIA expressão matemática qualquer e analise se está correta
# ((a + b) * c)  = 'está correta'
# ((a + b) * c)) = 'está errada'
expr = str(input('Expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
