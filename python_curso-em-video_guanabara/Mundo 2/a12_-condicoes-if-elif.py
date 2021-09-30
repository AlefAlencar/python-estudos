# AULA 12 CONDIÇÕES ANINHADAS
nome = str(input('Qual é o seu nome? '))
if nome =='Alef':
    print('Que belo nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Nome de gostosa :9')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))