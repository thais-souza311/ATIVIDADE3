import numpy as np


# função criaEntrada abrira o arquivo e retornara uma matriz numpy com os resultados,estao na pasta SaidaDados

def criaEntrada(inst):
    # localizacao do arquivo
    caminho = 'Lista1/Teste/' + inst + '.txt'

    # Abre o arquivo para leitura ('r')
    armazena = open(caminho, 'r')

    # funcao que armazena os dados na data
    data = np.loadtxt(armazena)

    return data
