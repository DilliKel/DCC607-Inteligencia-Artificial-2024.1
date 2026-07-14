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

def calcular_probabilidades(adjacencias):
    distancias = []
    feromonios = []
    
    for adj in adjacencias:
        for aresta in arestas:
            if aresta[0] == adj:
                distancias.append(aresta[2])
                feromonios.append(aresta[3])
    
    atratividades = [feromonio * (1 / distancia) for distancia, feromonio in zip(distancias, feromonios)]
    soma_atratividades = sum(atratividades)
    probabilidades = [atratividade / soma_atratividades for atratividade in atratividades]
    
    return probabilidades

def escolher_aresta(adjacencias):
    probabilidades = calcular_probabilidades(adjacencias)
    limites = []
    soma = 0
    
    for probabilidade in probabilidades:
        soma += probabilidade
        limites.append(soma)
    
    r = random.random()
    
    for i, limite in enumerate(limites):
        if r > limite:
            escolhida = i + 1
    
    return adjacencias[escolhida]

def gerar_caminho():
    caminho = []
    adjacencias = ['AB', 'AC', 'AD']
    
    inicial = escolher_aresta(adjacencias)
    caminho.append(inicial)
    
    if 'D' in caminho[-1]:
        return caminho
    
    while True:
        for aresta in arestas:
            if caminho[-1] == aresta[0]:
                adjacencias = aresta[1]
                
                if len(adjacencias) == 0:
                    break
                else:
                    adjacencia_escolhida = escolher_aresta(adjacencias)
                    caminho.append(adjacencia_escolhida)
        
        return caminho

def calcular_comprimento(caminho):
    comprimento_total = 0
    
    for no in caminho:
        for aresta in arestas:
            if no == aresta[0]:
                comprimento_total += aresta[2]
    
    return comprimento_total

def evaporar_feromonio(taxa_evaporacao):
    for aresta in arestas:
        aresta[3] *= (1 - taxa_evaporacao)

def atualizar_feromonio(formigas):
    for formiga in formigas:
        feromonio = 1 / calcular_comprimento(formiga)
        
        for no in formiga:
            for aresta in arestas:
                if aresta[0] == no:
                    aresta[3] += feromonio

# Configurações do ACO
melhor_formiga = None
melhor_comprimento = float('inf')
iteracoes = 30

# Execução do algoritmo ACO
for _ in range(iteracoes):
    evaporar_feromonio(0.3)
    formigas = []
    
    for _ in range(5):  # Criação de 5 formigas por iteração
        formiga = gerar_caminho()
        formigas.append(formiga)
        
        comprimento_formiga = calcular_comprimento(formiga)
        
        if comprimento_formiga < melhor_comprimento:
            melhor_formiga = formiga
            melhor_comprimento = comprimento_formiga
    
    atualizar_feromonio(formigas)

# Imprimir o melhor caminho encontrado
print("Melhor caminho encontrado:")
print(melhor_formiga)
print("Comprimento do caminho:", melhor_comprimento)
