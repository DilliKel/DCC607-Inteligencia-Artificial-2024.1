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

def probabs(adja):
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
        atract = fer[cont] * (1 / dists[cont])
        atratividades.append(atract)
        cont += 1
    
    soma = sum(atratividades)
    probs = []
    for i in atratividades:
        prob = i / soma
        probs.append(prob)
    return probs

def escolhaAresta(adjs):
    probab = probabs(adjs)
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

def formiga():
    caminho = []
    inicial = escolhaAresta(['AB', 'AC', 'AD', 'AE'])
    caminho.append(inicial)
    
    if 'D' in caminho[-1]:
        return caminho
    else:
        while True:
            for i in arestas:
                if caminho[-1] == i[0]:
                    adj = i[1]
                    if len(adj) == 0:
                        break
                    else:
                        adj_random = escolhaAresta(adj)
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
        for j in i:
            for k in arestas:
                if k[0] == j:
                    k[3] = k[3] + ferom

# Configurações do ACO
