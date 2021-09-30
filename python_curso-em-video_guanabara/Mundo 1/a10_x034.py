# LEIA: salário
# CALCULE: até R$1250 = +15%. Acima, +10%
# RETORNE: novo salário

sa = float(input('Salário atual: R$'))
faixa = 1250.00
ap1 = 15
ap2 = 10
if sa <= faixa:
    aum = sa * (ap1 / 100)
    ns = sa + aum
    ap = ap1
else:
    aum = sa * (ap2 / 100)
    ns = sa + aum
    ap = ap2
print('O salário era R${}. Você receberá um aumento de {}% (R${:.2f}). Seu novo salário é de R${:.2f}'.format(sa, ap, aum, ns))
