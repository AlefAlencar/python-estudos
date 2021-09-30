''' # SOBRE else EM while E for, ALÉM DO if
a = b = 0
while a < 100:
    a += 1
    print(f'a: {a}')
else:
    while b < 100:
        b += 1
        print(f'b: {b}')
    print('FIM')

print(f'\n#a: {a}'
      f'\n#b: {b}')'''

'''# SOBRE *args E **kwargs
def teste(*lista, **dicionario):
    print('LISTA, elementos: ', end='')
    for elemento in lista:
        print(f'{elemento},', end=' ')
    print()
    print('DICIONÁRIO, chave:valor: ', end='')
    for chave, valor in dicionario.items():
        print(f'{chave}:{valor},', end=' ')


print('\n# TESTE 1: args (elementos de lista) primeiro, kwargs (chaves:valores) depois')
teste(1, 2, 3, a=-1, b=-2, c=-3)
print()

print('\n# TESTE 2: args recebe uma lista, kwargs recebe um dicionário:')
lista1 = ['a', 'b', 'c']
dicio1 = {'a': -1, 'b': -2, 'c': -3}
teste(*lista1, **dicio1)
print()'''

'''var_global_0 = '#0.0 inicial var_global_0'
print('f0v0', var_global_0)


def funcao_nv1():
    var_local_1 = '#1.0 inicial var_local_1'
    print('n1v1', var_local_1)

    def funcao_nv2_so_local():
        var_local_2 = '#2.0 inicial var_local_2'
        print('n2v2', var_local_2)
        #print('n2v1', var_local_1)
        #print('n2v0', var_global_0)

        def funcao_nv3_so_local():
            var_local_3 = '#3.0 inicial var_local_3'
            print('n3v3', var_local_3)
            #print('n3v2', var_local_2)
            #print('n3v1', var_local_1)
            #print('n3v0', var_global_0)

        def funcao_nv3_acessa_nonlocal_1():
            nonlocal var_local_1
            var_local_1 = '#1.2 nonlocal var_local_1'
            print('n3v1', var_local_1)
            #print('n3v2', var_local_2)
            #print('n3v0', var_global_0)

        def funcao_nv3_acessa_nonlocal_2():
            nonlocal var_local_2
            var_local_2 = '#2.2 nonlocal var_local_2'
            print('n3v2', var_local_2)
            #print('n3v1', var_local_1)
            #print('n3v0', var_global_0)

        def funcao_nv3_acessa_global():
            global var_global
            var_global = '#0.1 global var_global_0'
            print('n3v0', var_global)
            #print('n3v1', var_local_1)
            #print('n3v2', var_local_2)

        funcao_nv3_so_local()
        funcao_nv3_acessa_nonlocal_1()
        funcao_nv3_acessa_nonlocal_2()
        funcao_nv3_acessa_global()

    def funcao_nv2_acessa_nonlocal():
        nonlocal var_local_1
        var_local_1 = '#1.3 nonlocal var_local_1'
        print('n2v1', var_local_1)

    def funcao_nv2_acessa_global():
        global var_global
        var_global = '#0.2 global var_global_0'
        print('n2v0', var_global)

    funcao_nv2_so_local()
    funcao_nv2_acessa_nonlocal()
    funcao_nv2_acessa_global()


funcao_nv1()'''


def nova_funcao():
    def funcao_interna_local():
        abrangencia = 'local'
        escopo_local = 'funcao_interna_local'

    def funcao_interna_nonlocal():
        nonlocal abrangencia
        abrangencia = 'primeiro nível'
        escopo_local = 'funcao_interna_nonlocal'

    def funcao_interna_global():
        global abrangencia
        abrangencia = 'global'
        escopo_local = 'funcao_interna_global'

    abrangencia = 'inicial'  # 1
    escopo_local = 'inicial'
    funcao_interna_local()
    print('Após função local:', abrangencia) # 2
    print('Após função local:', escopo_local)
    funcao_interna_nonlocal()
    print('Após função nonlocal:', abrangencia) # 3
    print('Após função nonlocal:', escopo_local)
    funcao_interna_global()
    print('Após função global:', abrangencia) # 4
    print('Após função global:', escopo_local)


# print(abrangencia)
nova_funcao()
print(abrangencia)
# print(escopo_local)
