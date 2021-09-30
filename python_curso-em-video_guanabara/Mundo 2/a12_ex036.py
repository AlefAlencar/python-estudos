# APROVANDO EMPRÉSTIMO
# LEIA: valor da casa; salário do comprador; quantos anos para pagar;
# RETORNE: valor da prestação mensal, máximo 30% do salário.
# Se ele não puder, negue o empréstimo.

valor = float(input('Qual o valor do imóvel? R$'))
anos = int(input('Em quantos anos pretende quitar? '))
salario = float(input('Qual é o seu salário? R$'))

meses = anos * 12;
mensalidade = valor / meses;

print('Você pretende quitar em {} anos, o que corresponde a {} meses. '
      '\nAssim, o valor da mensalidade será de R${:.2f}, equivalente a {:.2f}% de seu salário.'
      .format(anos, meses, mensalidade, mensalidade / salario * 100))
if mensalidade / salario <= 0.30:
    print('Portanto, o empréstimo está APROVADO. Parabéns!')
else:
    print('Infelizmente, o empréstimo foi NEGADO. Lamentamos.')