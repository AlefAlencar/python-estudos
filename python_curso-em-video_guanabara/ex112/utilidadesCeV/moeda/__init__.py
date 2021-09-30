def aumentar(numero=0.0, fator=0.0, formato=False):
    """
    Aumenta o valor conforme o fator percentual
    :param numero: valor
    :param fator: Porcentagem
    :param formato: True retorna valor formato em moeda R$
    :return: Valor formatado ou não
    """
    res = numero + (numero * fator/100)
    return res if not formato else moeda(res)


def diminuir(numero=0.0, fator=0.0, formato=False):
    """
        Aumenta o valor conforme o fator percentual
        :param numero: valor
        :param fator: Porcentagem
        :param formato: True retorna valor formato em moeda R$
        :return: Valor formatado ou não
    """
    res = numero - (numero * fator/100)
    return res if not formato else moeda(res)


def dobro(numero=0.0, formato=False):
    res = numero * 2
    return res if not formato else moeda(res)


def metade(numero=0.0, formato=False):
    res = numero / 2
    return res if not formato else moeda(res)


def moeda(valor=0.0):
    return f'R${valor:.2f}'.replace(".", ",")


def opcional(valor=0.0, opcao=True):
    if opcao:
        return moeda(valor)
    else:
        return valor


def resumo(preco, aumento, desconto):
    print(f'{"RESUMO DE VALOR":=^50}')
    print(f'{"Preço analisado:":.<20}{moeda(preco):.>30}\n'
          f'{"Dobro:":.<20}{dobro(preco,True):.>30}\n'
          f'{"Metade:":.<20}{metade(preco,True):.>30}\n'
          f'{"Aumento +"+str(aumento)+"%:":.<20}{aumentar(preco,aumento,True):.>30}\n'
          f'{"Desconto -"+str(desconto)+"%:":.<20}{diminuir(preco,desconto,True):.>30}')
    print(f'{"FIM":=^50}')
