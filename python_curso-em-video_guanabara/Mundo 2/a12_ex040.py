# MÉDIA DO ALUNO
# LEIA: duas notas.
# CALCULE: Média.
# RETORNE: Se <5.0 = Reprovado, 5.0<m<6.9 = Recuperação, >=7.0 = Aprovado.

print('Digite suas notas e veja qual a sua média: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digita a segunda nota: '))
media = (nota1 + nota2) / 2
rep = 4.9
rec = 6.9

print('Sua nota média foi {}. Você está: '.format(media))
if media <= rep:
    print('REPROVADO. Tente outra vez.')
elif media <= rec:
    print('EM RECUPERAÇÃO. Persista!')
else:
    print('APROVADO. Parabéns! :D')