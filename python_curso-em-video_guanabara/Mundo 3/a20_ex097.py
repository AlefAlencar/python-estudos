# FUNCAO escreva() recebe texto e imprime formatado com linhas do tamanho do texto:
# -------------
#  Olá, mundo!
# -------------
def escreva(texto):
    print(f'-{"-"*len(texto)}-')
    print(f' {texto} ')
    print(f'-{"-"*len(texto)}-')


# PRINCIPAL
escreva('Alef Alencar')
escreva('Samuel Alencar')
escreva('Makaulyn Alencar')
while True:
    escreva(str(input('Texto: ')))
