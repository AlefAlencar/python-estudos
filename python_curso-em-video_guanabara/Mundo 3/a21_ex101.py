# OBRIGATORIEDADE DO VOTO
# FUNCAO voto(ano_nasc) return = negado, opcional ou obrigatório
# retorne o valor literal (a frase)
def eleitor(ano):
    from datetime import date
    idade = date.today().year - ano
    status = ''
    if idade < 16:
        status = 'NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        status = 'OPCIONAL'
    else:
        status = 'OBRIGATÓRIO'
    return f'Com {idade} anos: voto {status}.'


ano_nasc = int(input('Digite seu ano de nascimento: '))
print(eleitor(ano_nasc))
