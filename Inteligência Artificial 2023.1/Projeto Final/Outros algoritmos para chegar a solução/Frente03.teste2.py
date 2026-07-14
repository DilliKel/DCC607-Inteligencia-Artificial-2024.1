import random

ab = ['AB', ['BC', 'BD', 'BE'], 8, 1]
ac = ['AC', ['CB', 'CD', 'CE'], 14, 1]
ad = ['AD', ['DE'], 22, 1]
ae = ['AE', [], 23, 1]

bc = ['BC', ['CD', 'CE'], 9, 1]
bd = ['BD', ['DC', 'DE'], 11, 1]
be = ['BE', [], 6, 1]

cb = ['CB', ['BD', 'BE'], 9, 1]
cd = ['CD', ['DE'], 10, 1]
ce = ['CE', [], 5, 1]

de = ['DE', [], 12, 1]
dc = ['DC', ['CE'], 10, 1]

arestas = [ab, ac, ad, ae, bc, bd, be, cb, cd, ce, de, dc]


def probabilidade_atracao(adjacentes):
    distancias = []
    feromonios = []

    for adjacente in adjacentes:
        for aresta in arestas:
            if aresta[0] == adjacente:
                distancias.append(aresta[2])
                feromonios.append(aresta[3])

    atratividades = [(feromonio * (1 / distancia)) for distancia, feromonio in zip(distancias, feromonios)]
    soma_atratividades = sum(atratividades)
    probabilidades = [(atracao / soma_atratividades) for atracao in atratividades]

    return probabilidades




def escolher_aresta(adjacentes):
    probabilidades = probabilidade_atracao(adjacentes)
    limiares = []
    soma = 0

    for probabilidade in probabilidades:
        soma += probabilidade
        limiares.append(soma)

    r = random.random()
    for i, limiar in enumerate(limiares):
        if r < limiar:
            return adjacentes[i]

def gerar_formiga():
    caminho = []
    inicial = escolher_aresta(['AB','AC', 'AD', 'AE'])
    caminho.append(inicial)

    if 'D' in caminho[-1]:
        return caminho
    else:
        while True:
            for aresta in arestas:
                if caminho[-1] == aresta[0]:
                    adjacentes = aresta[1]
                    if len(adjacentes) == 0:
                        break
                    else:
                        adjacente_escolhido = escolher_aresta(adjacentes)
                        caminho.append(adjacente_escolhido)
            return caminho
            break

def calcular_comprimento(formiga):
    soma = 0
    for vertice in formiga:
        for aresta in arestas:
            if vertice == aresta[0]:
                soma += aresta[2]
    return soma

def evaporar_feromonio(taxa_evaporacao):
    for aresta in arestas:
        aresta[3] *= (1 - taxa_evaporacao)

def atualizar_feromonio(formigas):
    for formiga in formigas:
        feromonio = 1 / calcular_comprimento(formiga)
        for vertice in formiga:
            for aresta in arestas:
                if aresta[0] == vertice:
                    aresta[3] += feromonio

evaporar_feromonio(0.9)

for aresta in arestas:
    print(aresta)

formigas = [['AB','BD'],['AD']]
atualizar_feromonio(formigas)

for aresta in arestas:
    print(aresta)

for _ in range(30):
    evaporar_feromonio(0.9)
    formigas = [gerar_formiga() for _ in range(5)]
    atualizar_feromonio(formigas)

for aresta in arestas:
    print(aresta[0], aresta[3])

for formiga in formigas:
    print(formiga)
