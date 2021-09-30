# GERENCIADOR DE PAGAMENTOS
# LEIA: preço, condição de pagamento;
# RETORNE: valor.
# à vista dinheiro/cheque: -10%,
# à vista cartão: -5%,
# 2x cartão: 0%,
# 3x ou mais cartão: +20%.

print('{:=^40}'.format(' GERENCIADOR DE PAGAMENTO$ '))
preco = float(input('Qual o preço do produto? (R$): '))
condicao = int(input('1 : à vista dinheiro/cheque \n'
                     '2 : à vista cartão \n'
                     '3 : 2x cartão \n'
                     '4 : 3x+ cartão \n'
                     'Qual será a opção de pagamento? '))
if condicao == 1:
    print('Pagamento à vista em dinheiro/cheque: desconto de 10%. O valor final será de R${:.2f}'.format(preco * 0.90))
elif condicao == 2:
    print('Pagamento à vista no cartão: desconto de 5%. O valor final será de R${:.2f}'.format(preco * 0.95))
elif condicao == 3:
    print('Pagamento em 2x no cartão: cada parcela de R${:.2f}. Total de R${:.2f}.'.format(preco / 2, preco))
elif condicao == 4:
    vezes = int(input('Pagamento em 3x+ cartão: Valor acrescido de 20%. Total R${:.2f} \n'
          'Em quantas vezes pretende pagar? '.format(preco*1.20)))
    print('Parcelado em {} vezes: Parcela de R${:.2f}. Valor total R${:.2f}'.format(vezes, preco*1.20/vezes, preco*1.20))
else:
    print('Opção inexistente. Tente novamente.')
print('Obrigado, volte sempre! :D')
