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

    

