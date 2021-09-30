# concatena o nome do convidado em uma nova linha no arquivo.
def gravar_nome_convidado(convidado):
    with open(nome_arquivo, 'a') as file_object:
        file_object.write(f'{convidado}\n')


# ler o arquivo lista de convidados.
def ler_arquivo(arquivo):
    with open(arquivo, 'r') as arquivo_convidados:
        lista_convidados = arquivo_convidados.readlines()
    return lista_convidados


# chama a função ler_arquivo e mostra a lista de convidados
def mostrar_convidados():
    lista_convidados = ler_arquivo(nome_arquivo)
    print('CONVIDADOS:')
    for n, convidado in enumerate(lista_convidados):
        print(f'{n+1}. {convidado.title()}', end='')


nome_arquivo = 'guest_book.txt'
opcao = ' '
continuar_programa = adicionar_mais = True

# PROGRAMA
while continuar_programa:
    # Pergunta a opção desejada.
    while opcao not in '123':
        opcao = str(input('OPÇÕES?\n'
                          '[1] Consultar lista\n'
                          '[2] Adicionar convidado(a)\n'
                          '[3] ENCERRAR programa\n'
                          'O que deseja fazer? ')).strip().upper()[0]
    if opcao == '1':
        mostrar_convidados()
    elif opcao == '2':
        # Pergunta o nome do convidado e grava no arquivo.
        while adicionar_mais:
            nome_convidado = str(input('NOME convidado(a):\n')).strip().lower()
            gravar_nome_convidado(nome_convidado)
            nome_convidado = resposta = ' '
            # Pergunta se adicionará novo convidado.
            while resposta not in 'SN':
                resposta = str(input('NOVO CONVIDADO(A)? [S/N]\n')).strip().upper()[0]
            if resposta == 'S':
                resposta = ' '
            elif resposta == 'N':
                adicionar_mais = False
    elif opcao == '3':
        continuar_programa = False
    opcao = ' '
