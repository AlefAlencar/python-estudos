import csv
from pygal_maps_world.i18n import COUNTRIES


class Arquivo:
    """Abertura e leitura de arquivo."""
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.arquivo = ''
        self.cabecalho = ''
        self.paises = []
        self.pibs = []
        self.paises_pibs = {}

    def carregar_arquivo(self):
        """Abre o arquivo e lê"""
        with open(self.nome_arquivo) as a:
            self.arquivo = csv.reader(a)
            self.ler_cabecalho()
            self.ler_dados()

    def ler_cabecalho(self):
        """Lê s salva o cabeçalho."""
        for i in range(0, 4):
            next(self.arquivo)
        self.cabecalho = next(self.arquivo)

    def ler_dados(self):
        """Lê os dados. (Chame ler_cabecalho antes para ler o cabeçalho).
        -> Salva os dados correspondentes ao ano na posicao_pib."""
        posicao_pais = 0
        primeiro_pib = 5
        posicao_pib = 64  # verifique a posição na lista
        pais, pib = '', 0
        for linha in self.arquivo:
            try:
                pais = linha[posicao_pais]
                for i in range(posicao_pib, primeiro_pib, -1):
                    if linha[i]:
                        pib = int(float(linha[i]))
                        break
            except ValueError:
                pib = 0
            self.paises.append(pais)
            self.pibs.append(pib)

    # FUNÇÕES DE EXIBIÇÃO DE DADOS
    def mostrar_cabecalho(self):
        """Mostra o cabeçalho 'cru' (conforme está no arquivo)."""
        print(self.cabecalho)

    def listar_cabecalho(self):
        """Exibe o cabeçalho em forma de lista numerada."""
        for indice, item in enumerate(self.cabecalho):
            print(f'{indice:>3}: {item:.>20}')

    def listar_nomes_pib(self):
        """Exibe o nome dos países e respectivos valores de PIB em 2020."""
        c = 0
        for indice, pais in enumerate(self.paises):
            print(f'{c:<3}-{pais:.<60}{self.pibs[indice]:.>20}')
            c += 1

    def criar_dicio_nome_pib(self):
        for i, pais in enumerate(self.paises):
            self.paises_pibs[pais] = self.pibs[i]


def pega_codigo_pais(nome_pais):
    """Devolve o código de duas letrar do Pygal para um país, dado o seu nome."""
    for codigo, nome in COUNTRIES.items():
        if nome_pais == nome:
            return codigo
    return None


def converter_para_trilhao(valor):
    """Converte o valor inteiro em trilhão com três casas decimais."""
    novo_valor = valor / 1000000000000
    novo_valor = float(f'{novo_valor:.3f}')  # define até 3 casas decimais
    return novo_valor


def cria_dicio_codigo_pib(lista):
    """Cria um novo dicionário de códigos Pygal de países com respectivos PIBs."""
    dicio_codigopais_pib = {}
    for nome, pib in lista.items():
        codigo = pega_codigo_pais(nome)
        if codigo is None:
            continue
        pib_bilhao = converter_para_trilhao(pib)
        dicio_codigopais_pib[codigo] = pib_bilhao
    return dicio_codigopais_pib


def listar_dicio_codigo_pib(lista):
    c = 0
    for codigo, pib in lista.items():
        print(f'{c:<3} = {codigo}:{pib:.>20}')
        c += 1
