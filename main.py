# libs utilizadas
# Thais Danieli Branco de Souza - 2021001228
import EntradaDados as ent
import SaidaDados as exit
import Inicializacao as ini
from Funcoes import (tipoGrafo as tg, verificaAdjacencia as va, calcDensidade as cd,
                     insereAresta as ia, removeAresta as ra, insereVertice as iv, removeVertice as rv)

if __name__ == '__main__':
    instancia = input("Digite a instância que gerará o grafo: ")
    inst = ent.criaEntrada(instancia)

    verificaAdja = va(inst, 0, 1)
    result = [instancia, inst, tg(inst), cd(inst)]
    exit.salvaResultado(result)

    print('Nome da instância:', instancia, '\n')
    print('Matriz correspondente: \n', inst, '\n')

    graph = ini.criaGrafo(inst)
    print(graph, '\n')

    print('Tipo e densidade do grafo:', '\n', tg(inst), '\n', cd(inst), '\n')

    # Insere a linha e a coluna, as quais inserirão ou removerão as arestas
    vi = int(input('Digite a linha: '))
    vj = int(input('Digite a coluna: '))
    print('\n')

    ia(inst, vi, vj)
    print('Aresta inserida:\n', inst, '\n')
    ini.visualizarGrafo(True, ini.criaGrafo(inst))

    ra(inst, vi, vj)
    print('Aresta removida: \n', inst, '\n')
    ini.visualizarGrafo(True, ini.criaGrafo(inst))
