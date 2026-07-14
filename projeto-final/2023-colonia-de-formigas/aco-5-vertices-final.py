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

def probabs(adja, capacidade):
    dists = []
    fer = []
    for i in adja:
        for j in arestas:
            if j[0] == i:
                dists.append(j[2])
                fer.append(j[3])
    
    atratividades = []
    cont = 0
    while cont < len(adja):
        if dists[cont] > capacidade:
            atract = 0
        else:
            atract = fer[cont] * (1 / dists[cont])
        atratividades.append(atract)
        cont += 1
    
    soma = sum(atratividades)
    probs = []
    for i in atratividades:
        prob = i / soma
        probs.append(prob)
    return probs

def escolhaAresta(adjs, capacidade):
    probab = probabs(adjs, capacidade)
    limiares = []
    soma = 0
    for i in probab:
        soma += i
        limiares.append(soma)
    r = random.random()
    cont = 0
    for i in limiares:
        if r > i:
            cont += 1
    return adjs[cont]

def formiga(capacidade):
    caminho = []
    inicial = escolhaAresta(['AB', 'AC', 'AD', 'AE'], capacidade)
    caminho.append(inicial)
    
    if 'E' in caminho[-1]:
        return caminho
    else:
        while True:
            for i in arestas:
                if caminho[-1] == i[0]:
                    adj = i[1]
                    if len(adj) == 0:
                        break
                    else:
                        adj_random = escolhaAresta(adj, capacidade)
                        caminho.append(adj_random)
            return caminho
            break

def comprimento(formiga):
    soma = 0
    for i in formiga:
        for j in arestas:
            if i == j[0]:
                soma += j[2]
    return soma

def evaporacao(evap):
    for i in arestas:
        i[3] = i[3] * (1 - evap)

def atualiza_ferom(formigas):
    for i in formigas:
        ferom = 1 / comprimento(i)
        for j in arestas:
            if j[0] in i:
                j[3] += ferom

def imprime_feromonios(arestas):
    for a in arestas:
        print(f"Feromônio na aresta {a[0]}-{a[1]}: {a[3]}")

def aco(num_formigas, num_iteracoes, capacidade, evap):
    melhor_caminho = None
    melhor_comprimento = float('inf')

    for _ in range(num_iteracoes):
        formigas = []
        for _ in range(num_formigas):
            formiga_atual = formiga(capacidade)
            formigas.append(formiga_atual)

            if 'D' in formiga_atual[-1] and comprimento(formiga_atual) < melhor_comprimento:
                melhor_caminho = formiga_atual
                melhor_comprimento = comprimento(formiga_atual)

        atualiza_ferom(formigas)
        evaporacao(evap)

    imprime_feromonios(arestas)

    return melhor_caminho

# Exemplo de utilização
melhor_rota = aco(num_formigas=10, num_iteracoes=100, capacidade=20, evap=0.1)

print("----------------------------------------------------")
print("Melhor rota encontrada:", melhor_rota)
print("Comprimento da rota:", comprimento(melhor_rota))

