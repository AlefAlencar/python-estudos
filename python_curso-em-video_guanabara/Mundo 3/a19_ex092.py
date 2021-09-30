# CADASTRO DE TRABALHADOR
# LEIA nome, ano_nascimento (guarde a idade), carteira de trabalho CTPS
# CADASTRE-OS num dicionário
# Se a CTPS != 0, o dict receberá também o ano_contratação, e salário.
# Acrescente com quantos anos a pessoas vai se aposentar
# cadastro{nome, idade, ctps, ano_contrat, salario, idade_aposent}
import datetime
trabalhador = {'Nome': str(input('NOME: ')).strip(),
               'Idade': datetime.date.today().year - int(input('ANO DE NASCIMENTO: ')),
               'CTPS': int(input('CTPS [0 se não tiver]: '))}
if trabalhador['CTPS'] != 0:
    trabalhador['Ano de contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    trabalhador['Salário'] = float(input('SALÁRIO: R$'))
    trabalhador['Idade de aposentadoria'] = (trabalhador['Ano de contratação'] + 35) - (datetime.date.today().year - trabalhador['Idade'])

print('='*30, trabalhador)
for k, v in trabalhador.items():
    print(f'{k}: {v}')
