import random

# Definição das arestas do grafo
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

# Função para calcular as probabilidades das arestas adjacentes
def calcular_probabilidades(adjacentes):
    distancias = []
    feromonios = []
    
    # Obtém as distâncias e os feromônios das arestas adjacentes
    for adjacente in adjacentes:
        for aresta in arestas:
            if aresta[0] == adjacente:
                distancias.append(aresta[2])
                feromonios.append(aresta[3])
    
    # Calcula as atratividades das arestas
    atratividades = []
    total_atratividade = 0
    for i in range(len(adjacentes)):
        atratividade = feromonios[i] * (1 / distancias[i])
        atratividades.append(atratividade)
        total_atratividade += atratividade
    
    # Calcula as probabilidades de escolha das arestas
    probabilidades = []
    for atratividade in atratividades:
        probabilidade = atratividade / total_atratividade
        probabilidades.append(probabilidade)
    
    return probabilidades

# Função para escolher uma aresta com base nas probabilidades
def escolher_aresta(adjacentes):
    probabilidades = calcular_probabilidades(adjacentes)
    limites = []
    soma = 0
    
    # Calcula os limites para escolha aleatória
    for probabilidade in probabilidades:
        soma += probabilidade
        limites.append(soma)
    
    # Escolhe uma aresta aleatoriamente com base nos limites
    aleatorio = random.random()
    indice_escolhido = 0
    
    for limite in limites:
        if aleatorio > limite:
            indice_escolhido += 1
    
    return adjacentes[indice_escolhido]

# Função para gerar um caminho possível para uma formiga
def gerar_caminho():
    caminho = []
    adjacentes = ['AB', 'AC', 'AD']  # Arestas iniciais
    
    # Escolhe a aresta inicial
    inicial = escolher_aresta(adjacentes)
    caminho.append(inicial)
    
    # Verifica se o destino final 'D' já foi alcançado
    if 'D' in caminho[-1]:
        return caminho
    else:
        # Gera o restante do caminho até alcançar o destino final 'D'
        while True:
            for aresta in arestas:
                if caminho[-1] == aresta[0]:
                    adjacentes = aresta[1]
                    
                    # Verifica se não há mais arestas adjacentes disponíveis
                    if len(adjacentes) == 0:
                        break
                    else:
                        adjacente_escolhida = escolher_aresta(adjacentes)
                        caminho.append(adjacente_escolhida)
            
            return caminho
            break

# Função para calcular o comprimento total de um caminho
def calcular_comprimento(caminho):
    soma = 0
    for aresta in caminho:
        for aresta_grafo in arestas:
            if aresta == aresta_grafo[0]:
                soma += aresta_grafo[2]
    return soma

# Função para evaporar o feromônio em todas as arestas
def evaporar_feromonio(taxa_evaporacao):
    for aresta in arestas:
        aresta[3] = aresta[3] * (1 - taxa_evaporacao)

# Função para atualizar o feromônio nas arestas percorridas pelas formigas
def atualizar_feromonio(formigas):
    for formiga in formigas:
        feromonio = 1 / calcular_comprimento(formiga)
        for aresta_formiga in formiga:
            for aresta_grafo in arestas:
                if aresta_grafo[0] == aresta_formiga:
                    aresta_grafo[3] += feromonio

# Execução do algoritmo ACO
for _ in range(30):
    evaporar_feromonio(0.3)
    formigas = []
    
    # Gerar 5 formigas em cada iteração
    for _ in range(5):
        formigas.append(gerar_caminho())
    
    atualizar_feromonio(formigas)

# Imprime os valores finais de feromônio nas arestas
for aresta in arestas:
    print(aresta[0], aresta[3])

# Imprime as formigas geradas
for formiga in formigas:
    print(formiga)
