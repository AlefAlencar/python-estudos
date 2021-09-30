# LEIA 5 números e cadastre na lista
# Cadastre já na posição correta em ordem, sem usar o .sort()
lista = []
valor = 0  # t = 0
resp = ' '
for c in range(0, 5):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        p = 0
        while p < len(lista):
            if valor < lista[p]:
                lista.insert(p, valor)
                break
            p += 1
print(f'LISTA: {lista}')


'''while True:
    valor = int(input('Digite valor: '))
    if t == 0:
        valores.append(valor)
    elif t == 1:
        if valor < valores[0]:
            valores.insert(0, valor)
        else:
            valores.append(valor)
    else:
        c = 0
        while c <= t:
            if valor <= valores[c]:
                valores.insert(c, valor)
                break
            else:
                c += 1
            if c == t:
                valores.append(valor)
    while resp not in 'SN':
        resp = str(input('CONTINUAR? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    resp = ' '
    t += 1
print(valores)'''
