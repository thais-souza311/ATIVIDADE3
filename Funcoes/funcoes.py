import igraph as ig
import numpy as np
import matplotlib as plot


def tipoGrafo(inst):
    type = int

    matrixLaco = laco(inst)
    matrixParalela = arestaParalela(inst)
    matrixDirecionada = direcionada(inst)

    if matrixLaco != True and (matrixParalela != True or matrixDirecionada != True):
        type = 0  # Simples
    elif matrixDirecionada == True and not matrixLaco and matrixParalela:
        type = 1  # Digrafo
    elif matrixDirecionada != False and matrixParalela == True and matrixLaco != True:
        type = 2  # Multigrafo
    elif matrixDirecionada != False and matrixParalela == True and matrixLaco == True:
        type = 3  # Pseudografo

    return type


def laco(matrix):
    laco = False

    for i in range(matrix.shape[0]):
        laco = matrix[i][i] != 0
        if laco:
            break
    return laco


def arestaParalela(matrix):
    paralela = False

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] == matrix[j][i]:
                paralela = True
            else:
                paralela = False
    return paralela


def direcionada(matrix):
    direcionada = False

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i][j] != matrix[j][i]:
                direcionada = True
            else:
                direcionada = False
    return direcionada


def verificaAdjacencia(inst, vi, vj):
    if inst[vi][vj] > 0:  # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes


def calcDensidade(inst):
    type = tipoGrafo(inst)

    aresta = 0

    for i in range(inst.shape[0]):
        for j in range(inst.shape[1]):
            if inst[i][j] != 0:
                aresta += 1

    if type == 0:
        density = (2 * aresta) / (inst.shape[0] * (inst.shape[0] - 1))  # formula do slide
        return float(density)
    elif type == 1:
        density = aresta / (inst.shape[0] * (inst.shape[0] - 1))  # formula do slide
        return float(density)
    else:
        return print("Densidade nao pode ser calculada!")


def insereAresta(inst, vi, vj):
    newMatrixA =  inst
    newMatrixA[vi][vj] += 1
    return newMatrixA


def insereVertice(inst, vi, vj):
    inst.add_vertex(vi, vj)
    return inst

def removeAresta(inst, vi, vj):
    newMatrixRA = inst
    newMatrixRA[vi][vj] = 0
    return newMatrixRA


def removeVertice(inst, vi, vj):
    inst.delete_vertex(vi, vj)
    return inst
