'''filename = 'pi_digits.txt'
# abrir e armazenar cada linha em uma lista 'lines'
with open(filename) as file_object:
    lines = file_object.readlines()
# laço acrescenta cada linha (em 'lines') e armazena na variável 'pi_string' sem o caractere de quebra de linha ('\n')
pi_string = ''
for line in lines:
    pi_string += line.strip()
# exibe a string
print(pi_string)
print(len(pi_string))'''

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f'{pi_string[:52]}...')
