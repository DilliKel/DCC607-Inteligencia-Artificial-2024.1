import random

ab = ['AB',['BC','BD'],8,1,10]
ac = ['AC',['BC','BD'],14,1,15]
ad = ['AD',[],22,1,5]
bc = ['BC',['CD'],9,1,20]
cb = ['CB',['BD'],9,1,25]
bd = ['BD',[],8,1,10]
cd = ['CD',[],10,1,15]

arestas = [ab, ac, ad, bc, cb, bd, cd]

def probabilidade_atracao(adjacentes, capacidade_disponivel):
    distancias = []
    feromonios = []
    demandas = []

    for adjacente in adjacentes:
        for aresta in arestas:
            if aresta[0] == adjacente:
                distancias.append(aresta[2])
                feromonios.append(aresta[3])
                demandas.append(aresta[4])

    atratividades = [(feromonio * (1 / distancia) * (demanda / capacidade_disponivel)) for distancia, feromonio, demanda in zip(distancias, feromonios, demandas)]
    soma_atratividades = sum(atratividades)
    probabilidades = [(atracao / soma_atratividades) for atracao in atratividades]

    return probabilidades

def escolher_aresta(adjacentes, capacidade_disponivel):
    probabilidades = probabilidade_atracao(adjacentes, capacidade_disponivel)
    limiares = []
    soma = 0

    for probabilidade in probabilidades:
        soma += probabilidade
        limiares.append(soma)

    r = random.random()
    for i, limiar in enumerate(limiares):
        if r < limiar:
            return adjacentes[i]

def gerar_formiga(capacidade_maxima):
    caminho = []
    inicial = escolher_aresta(['AB','AC','AD'], capacidade_maxima)
    caminho.append(inicial)

    capacidade_disponivel = capacidade_maxima - inicial[3]  # Corrigido para obter a capacidade disponível corretamente

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
                        adjacente_escolhido = escolher_aresta(adjacentes, capacidade_disponivel)
                        caminho.append(adjacente_escolhido)
                        capacidade_disponivel -= adjacente_escolhido[3]  # Corrigido para subtrair a capacidade da aresta escolhida
            return caminho
            break

def calcular_comprimento(formiga):
    soma = 0
    for vertice in formiga:
        for aresta in arestas:
            if aresta[0] == vertice:
                soma += aresta[2]
    return soma

def evaporar_feromonio(taxa_evaporacao):
    for aresta in arestas:
        aresta[3] *= (1 - taxa_evaporacao)

def atualizar_feromonio(formigas):
    for formiga in formigas:
        for vertice in formiga:
            for aresta in arestas:
                if aresta[0] == vertice:
                    aresta[3] += (1 / calcular_comprimento(formiga))

capacidade_maxima_veiculo = 50
taxa_evaporacao = 0.3
max_iteracoes = 30
formigas_por_iteracao = 5

for _ in range(max_iteracoes):
    evaporar_feromonio(taxa_evaporacao)
    formigas = []
    for _ in range(formigas_por_iteracao):
        formigas.append(gerar_formiga(capacidade_maxima_veiculo))
    atualizar_feromonio(formigas)

for aresta in arestas:
    print(aresta[0], aresta[3])

for formiga in formigas:
    print(formiga)
