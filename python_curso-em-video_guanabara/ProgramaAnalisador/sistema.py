from Arquivo import *
from Interface import *
from Arquivo import *
lista_opcoes = ['VISUALIZAR', 'CADASTRAR', 'SAIR']

nome_arquivo = 'arquivinho.txt'
if not ver_exist_arq(nome_arquivo):
    criar_arq(nome_arquivo)

while True:
    linha('SISTEMA', carac_padrao='*', linha_inferior=True, linha_superior=True)
    opcao_escolhida = menu(lista_opcoes)
    if opcao_escolhida == 1:
        print('Opção 1 - VISUALIZAR')
    elif opcao_escolhida == 2:
        print('Opção 2 - CADASTRAR')
    elif opcao_escolhida == 3:
        print("SAIR do Sistema. ENCERRADO")
        break
