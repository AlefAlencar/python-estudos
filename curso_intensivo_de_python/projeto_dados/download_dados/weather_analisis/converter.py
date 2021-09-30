import csv
from datetime import datetime


def fahrenheit_to_celsius(graus_fahrenheit):
    """Recebe a temperatura em graus Fahrenheit e converte para graus Celsius."""
    graus_celsius = (graus_fahrenheit - 32) * 5/9
    return graus_celsius


def inch_to_milimeters(polegada):
    """Recebe a medida em polegadas e converte para milímetros"""
    milimetro = polegada * 25.4
    return milimetro


# ABERTURA E LEITURA DE ARQUIVO
class Arquivo:
    def __init__(self, nome_arquivo):  # , leitor, cabecalho, datas, temps_max, temps_min):
        """Inicializa os atributos"""
        self.nome_arquivo = nome_arquivo
        self.leitor = ''
        self.cabecalho = ''
        self.datas = []
        self.temps_max = []
        self.temps_min = []

    def carregar_dados(self):
        """Carrega os dados do arquivo."""
        self.abrir_arquivo()

    def abrir_arquivo(self):
        """Abre o arquivo e chama ler_arquivo."""
        with open(self.nome_arquivo) as obj:  # LÊ O OBJETO E ARMAZENA COMO 'obj'
            self.leitor = csv.reader(obj)  # LÊ O OBJETO COM csv E ARMAZENA NUMA VARIÁVEL
            self.ler_dados()

    def ler_dados(self):
        """Lê o cabeçalho e salva os dados desejados em suas respectivas listas."""
        self.cabecalho = next(self.leitor)
        for linha in self.leitor:  # PEGA CADA DADO, DEPOIS ADICIONA NA RESPECT LISTA
            try:
                data = datetime.strptime(linha[0], '%Y-%m-%d')
                tmax = int(linha[1])
                tmin = int(linha[3])
            except ValueError:
                print(data, ': dados ausentes')
            else:
                self.datas.append(data)
                self.temps_max.append(tmax)
                self.temps_min.append(tmin)

    def imprimir_cabecalho(self):
        """Imprime o cabeçalho do arquivo csv"""
        print(f"Cabeçalho de '{self.nome_arquivo}'")
        for indice, item in enumerate(self.cabecalho):
            print(f"{indice:<3}: {item}")

    def imprimir_dados(self):
        """Imprime os dados salvos."""
        print('Alguns dados salvos:')
        for indice, data in enumerate(self.datas):
            print(f"{data}: {self.temps_max[indice]} - {self.temps_min[indice]}")
