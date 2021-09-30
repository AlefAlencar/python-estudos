# CRIE TUPLA com nomes de produtos e seus preços, na sequência ('Produto', 0.00, ...)
# MOSTRE: listagem de preços, organize de forma tabular
# Produto............R$   0.00
# Produto2...........R$   0.00
# ...
tupla = ('Notebook', 5000, 'Mouse Gamer', 150, 'Mousepad', 30, 'Headphones', 250, 'Cadeira Gamer', 500,
         'Mesa ARRD', 300, 'Caixas de som', 300, 'Estabilizador', 300)
print('LISTAGEM')
c = 0
for c in range(0, len(tupla), 2):
    # print(f'{tupla[c]}{"."*(30-len(tupla[c]))}R${" "*(8-len(tupla[c+1]))}{tupla[c+1]}')
    print(f'{tupla[c]:.<30}R${tupla[c+1]:>8.2f}')
print('='*30, 'FIM')
