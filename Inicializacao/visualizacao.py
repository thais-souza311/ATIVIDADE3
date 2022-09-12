import igraph
import numpy as np


def visualizarGrafo(execucao, grafo):
    if execucao == True:  # True para visualizar a imagem ou False
        grafo.vs[0]
        layout = grafo.layout("fr")  # Layouts: kk, drl, fr, tree
        visual_style = {}  # Vetor com as características visuais do grafo
        visual_style["vertex_size"] = 40  # Tamanho do vértice
        visual_style["vertex_shape"] = "circle"  # Formatos: triangle, circle, square
        visual_style["vertex_label_size"] = 20  # Tamanho do rótulo do vértice
        visual_style["margin"] = 30  # Margem do grafo em relação a borda da figura.
        grafo.vs["color"] = str(
            '#') + '33FF00'  # Cores: Az=99CCFF; Cinz=CCCCCC ; Am=FFFF00; Vd=33FF00; Lar=FFCC00; Ros=FF00FF
        visual_style["autocurve"] = True  # Considera arestas curvas. False para arestas retas.
        igraph.plot(grafo, layout=layout, **visual_style)
    return


def criaGrafo(matriz):
    qtdVertices = np.shape(matriz)[0]
    grafo = igraph.Graph()  # Cria objeto igraph inicialmente vazio
    grafo.add_vertices(qtdVertices)  # Adiciona vértices ao grafo
    grafo.vs["label"] = range(0, grafo.vcount())  # Define o nome de cada nó como um número inteiro
    for vi in range(0, qtdVertices):  # Para cada vértice vi
        for vj in range(vi + 1, qtdVertices):  # Para cada vértice vj
            controle = matriz[vi][vj]
            while controle > 0:  # Adiciona a quantidade de arestas paralelas ou peso da aresta
                grafo.add_edges([(vi, vj)])
                controle -= 1
    return grafo


def criaMatrizAdjacencias(instancia):
    print('NOME DA INSTÂNCIA:', instancia, '\n')
    caminho = 'D:/01-Academicos/01-UNIFEI/Disciplinas/SIN110 - Algoritmos e Grafos/Aulas/Codigos/grafo/Instancias/' + instancia + '.txt'
    with open(caminho, 'rb') as f:
        data = np.genfromtxt(f, dtype="int64")  # OBS. Lê arquivo .txt de uma Instancia no formato Matriz de Adjacência
    return data


def salvaResultado(resultado):
    stringRes = ''
    for res in resultado:
        stringRes += str(res) + ' '
    arquivo = open(
        'D:/01-Academicos/01-UNIFEI/Disciplinas/SIN110 - Algoritmos e Grafos/Aulas/Codigos/grafo/Resultados/resultado.txt',
        'a+')
    arquivo.writelines(stringRes + '\n')
    arquivo.close()
