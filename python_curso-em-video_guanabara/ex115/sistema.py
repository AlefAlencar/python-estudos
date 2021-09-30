from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver cadastrados', 'Cadastrar', 'SAIR'])
    if resposta == 1:
        # opção LISTAR CONTEÚDO de um Arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # opção CADASTRAR NOVA PESSOA
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Opção inválida\033[m')
    sleep(1)
