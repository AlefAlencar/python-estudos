# modelo03.py

# Atributos, instâncias, tipos e relacionamentos (associações UML, orientação a objetos)

class Computador:
    def __init__(self, codigo, nome, aquisicao, vida, marca):
        self.codigo = codigo
        self.nome = nome
        self.aquisicao = aquisicao
        self.vida = vida
        self.marca = marca

    def alerta_manutencao(self):
        # TODO: calcular período de manutenção.
        pass


class Marca:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome


# Instâncias(objetos) de marca.
dell = Marca(1, 'Dell')
hp = Marca(2, 'HP')
# Instâncias(objetos) de computador.
vostro = Computador(1, 'Vostro', '10/01/2015', 365, dell)
pavilion = Computador(2, 'Pavilion', '10/01/2015', 365, hp)

# PARA VER A ASSOCIAÇÃO DE OBJETOS ("Computador tem: Marca")
print("'", vostro.codigo, vostro.nome, vostro.aquisicao, vostro.vida, vostro.marca, "|||",
      vostro.marca.codigo, vostro.marca.nome, "'")

# EXEMPLOS DE TIPOS E ASSOCIAÇÕES DE OBJETOS
print('\nMOSTRE O TIPO DO OBJETO')
print('1 type (dell):\n', type(dell))
print('1 type(hp):\n', type(hp))
# <class '__main__.Marca'>
print('2 type(vostro):\n', type(vostro))
print('2 type(pavilion):\n', type(pavilion))
# <class '__main__.Computador'>
print('type(vostro.alerta_manutencao):\n', type(vostro.alerta_manutencao()))

print('\nPERGUNTA SE x É INSTÂNCIA DE a')
print('3 isinstance(dell, Marca):\n', isinstance(dell, Marca))
print('3 isinstance(hp, Marca):\n', isinstance(hp, Marca))
# True
print('4 isinstance(pavilion, Computador):\n', isinstance(pavilion, Computador))
print('4 isinstance(vostro, Computador):\n', isinstance(vostro, Computador))
# True

print('3 isinstance(dell, Computador):\n', isinstance(dell, Computador))
print('3 isinstance(hp, Computador):\n', isinstance(hp, Computador))
# False
print('4 isinstance(pavilion, Marca):\n', isinstance(pavilion, Marca))
print('4 isinstance(vostro, Marca):\n', isinstance(vostro, Marca))
# False

# Nesse exemplo, além da criação dos objetos existe uma sutileza: estamos criando uma
# associação chamada “Computador tem Marca”. Primeiro um objeto da classe “marca” (dell) é
# passado para a classe “computador” (vostro).
# Observe que na definição da classe “computador” essa associação foi criada através
# do comando: self.marca = marca.'''
