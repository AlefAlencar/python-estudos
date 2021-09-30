# DETECTOR DE PALÍNDROMO
# LEIA: frase
# RETORNE: é palíndromo ou não (que é possível ler de trás pra frente, sem espaços)

frase = str(input('Digite a frase e descubra se é palíndromo: ')).upper()
f = frase.replace(" ", "")
inv = f[::-1]
print('Sem espaços: ' + f)
print('Invertido  : ' + inv)
# print(frase)
if f == inv:
    print('PALÍNDROMO')
else:
    print('NÃO é palíndromo')
