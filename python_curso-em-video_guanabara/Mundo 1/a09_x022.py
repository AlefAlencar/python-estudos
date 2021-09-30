# LEIA: nome completo.
# RETORNE: nome todas as letra maiúsculas;
# nome com todas minúsculas;
# quantas letras, sem espaços;
# quantas letras tem o primeiro nome.

nome = str(input('Digite nome completo: '))
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
completo = list(nome.split())
print(len(completo[0]))
print(nome.find(' '))