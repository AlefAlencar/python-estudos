# LEIA: cidade.
# RETORNE: se começa ou não com 'santo'.

cid = str(input('Digite o nome da cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')