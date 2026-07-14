# Pseudocódigos — Algoritmos de Busca e IA

Pseudocódigos dos principais algoritmos estudados na disciplina.

## Busca em Largura (BFS)

```
busca_em_largura(inicio, objetivo):
    fila = [inicio]
    visitado = {inicio}

    enquanto fila não está vazia:
        nó = fila.pop(0)

        se nó = objetivo:
            retorne nó

        para cada vizinho em nó.vizinhos:
            se vizinho não está em visitado:
                visitado.adicione(vizinho)
                fila.append(vizinho)

    retorne "Objetivo não encontrado"
```

## Busca em Profundidade (DFS)

```
busca_em_profundidade(nó, objetivo):
    se nó = objetivo:
        retorne nó

    para cada vizinho em nó.vizinhos:
        resultado = busca_em_profundidade(vizinho, objetivo)

        se resultado ≠ "Objetivo não encontrado":
            retorne resultado

    retorne "Objetivo não encontrado"
```

## Busca em Profundidade Limitada

```
busca_em_profundidade_limitada(nó, objetivo, limite):
    se nó = objetivo:
        retorne nó

    se limite = 0:
        retorne "Limite de profundidade atingido"

    para cada vizinho em nó.vizinhos:
        resultado = busca_em_profundidade_limitada(vizinho, objetivo, limite - 1)

        se resultado ≠ "Limite de profundidade atingido" e resultado ≠ "Objetivo não encontrado":
            retorne resultado

    retorne "Objetivo não encontrado"
```

## Aprofundamento Iterativo (IDDFS)

```
busca_de_aprofundamento_iterativo(inicio, objetivo):
    limite = 0

    enquanto verdadeiro:
        resultado = busca_em_profundidade_limitada(inicio, objetivo, limite)

        se resultado ≠ "Limite de profundidade atingido":
            retorne resultado

        limite += 1
```

## Custo Uniforme

```
busca_de_custo_uniforme(inicio, objetivo):
    fila_prioridade = {inicio}
    custo = {inicio: 0}

    enquanto fila_prioridade não está vazia:
        nó = fila_prioridade.remove_min()

        se nó = objetivo:
            retorne nó

        para cada vizinho em nó.vizinhos:
            novo_custo = custo[nó] + custo(nó, vizinho)

            se vizinho não está em custo ou novo_custo < custo[vizinho]:
                custo[vizinho] = novo_custo
                fila_prioridade.update(vizinho, novo_custo)

    retorne "Objetivo não encontrado"
```

## Dijkstra

```
função dijkstra(grafo, inicio):
    distancias <- inicializarDistancias(inicio)  # Distância estimada do nó inicial para cada nó do grafo
    visitados <- criarConjuntoVazio()
    filaPrioridade <- criarFilaPrioridade()  # Fila de prioridade para selecionar o nó com a menor distância

    adicionarNaFilaPrioridade(filaPrioridade, (inicio, 0))  # Insere o nó inicial com distância zero na fila

    enquanto não vazio(filaPrioridade) faça:
        no, distancia <- removerDaFilaPrioridade(filaPrioridade)  # Seleciona o nó com menor distância
        adicionar em visitados

        para cada vizinho, peso em obterVizinhos(grafo, no) faça:
            novaDistancia <- distancia + peso

            se novaDistancia < distancias[vizinho] então:
                distancias[vizinho] <- novaDistancia
                adicionarNaFilaPrioridade(filaPrioridade, (vizinho, novaDistancia))

    retornar distancias

função obterVizinhos(grafo, no):
    # Retorna os vizinhos do nó no grafo com seus respectivos pesos
    ...

grafo <- obterGrafo()  # Obter o grafo com nós e arestas
inicio <- obterNoInicial()  # Obter o nó inicial para iniciar o algoritmo

distancias <- dijkstra(grafo, inicio)

imprimir "Distâncias mínimas:"
para cada no, distancia em distancias faça:
    imprimir "Distância de", inicio, "para", no, ":", distancia
```

## A* (A Estrela)

```
A_estrela(grafo, inicio, alvo):
    lista_fechada = vazia
    lista_aberta = [inicio]
    g[inicio] = 0
    f[inicio] = g[inicio] + h(inicio, alvo)

    enquanto lista_aberta não está vazia:
        u = nó com o menor valor f[u] em lista_aberta
        remova u de lista_aberta
        adicione u em lista_fechada

        se u = alvo então
            retorne o caminho reconstruído de inicio até alvo

        para cada vizinho v de u:
            se v está em lista_fechada, então
                continue

            novo_g = g[u] + custo(u, v)  // custo para chegar ao vizinho v a partir de u
            se v não está em lista_aberta ou novo_g < g[v]:
                g[v] = novo_g
                f[v] = g[v] + h(v, alvo)
                se v não está em lista_aberta, então
                    adicione v em lista_aberta

    // Não há caminho possível até o alvo
    retorne "Caminho não encontrado"
```

## N-Rainhas (Backtracking)

```
função resolverNRainhas(N):
    solucao <- criarTabuleiroVazio(N)  # Cria um tabuleiro vazio NxN
    coluna <- 0

    se posicionarRainhas(solucao, coluna, N) então:
        retornar solucao  # Solução encontrada
    senão:
        retornar "Não foi possível encontrar solução"

função posicionarRainhas(tabuleiro, coluna, N):
    se coluna >= N então:
        retornar verdadeiro  # Todas as rainhas foram posicionadas

    para cada linha de 0 a N-1 faça:
        se éPosicaoSegura(tabuleiro, linha, coluna, N) então:
            tabuleiro[linha][coluna] <- 'Q'  # Posiciona a rainha no tabuleiro

            se posicionarRainhas(tabuleiro, coluna + 1, N) então:
                retornar verdadeiro  # Rainha posicionada com sucesso

            tabuleiro[linha][coluna] <- '.'  # Remove a rainha do tabuleiro (backtracking)

    retornar falso  # Nenhuma posição segura encontrada para a rainha atual

função éPosicaoSegura(tabuleiro, linha, coluna, N):
    # Verifica se é seguro posicionar uma rainha na posição (linha, coluna) do tabuleiro

    # Verifica se não há outra rainha na mesma linha
    para cada col de 0 a coluna-1 faça:
        se tabuleiro[linha][col] == 'Q' então:
            retornar falso

    # Verifica se não há outra rainha na mesma diagonal superior esquerda
    i, j <- linha-1, coluna-1
    enquanto i >= 0 e j >= 0 faça:
        se tabuleiro[i][j] == 'Q' então:
            retornar falso
        i <- i-1
        j <- j-1

    # Verifica se não há outra rainha na mesma diagonal inferior esquerda
    i, j <- linha+1, coluna-1
    enquanto i < N e j >= 0 faça:
        se tabuleiro[i][j] == 'Q' então:
            retornar falso
        i <- i+1
        j <- j-1

    retornar verdadeiro  # Posição segura para posicionar a rainha

N <- obterValorN()  # Obter o valor N para o problema das N rainhas

solucao <- resolverNRainhas(N)

se solucao != "Não foi possível encontrar solução" então:
    imprimir "Solução encontrada:"
    imprimir solucao
senão:
    imprimir "Não foi possível encontrar uma solução."
```

> Nota: este é o pseudocódigo de N-Rainhas por backtracking, estudado em aula. As implementações práticas da disciplina (ver [`atividades/04-algoritmos-geneticos/`](../atividades/04-algoritmos-geneticos/)) resolvem o mesmo problema com algoritmos genéticos.

## 8-Puzzle via BFS

```
função resolverQuebraCabeca(estadoInicial, estadoObjetivo):
    fila <- criarFila()
    visitados <- criarConjuntoVazio()

    adicionarNaFila(fila, (estadoInicial, []))  # (estado, ações)

    enquanto não vazio(fila) faça:
        estado, acoes <- removerDaFila(fila)

        se estado == estadoObjetivo então:
            retornar acoes  # Solução encontrada

        adicionar estado em visitados

        para cada acao em obterAcoesPossiveis(estado) faça:
            novoEstado <- executarAcao(estado, acao)

            se novoEstado não está em visitados então:
                adicionarNaFila(fila, (novoEstado, acoes + [acao]))

    retornar "Não foi possível encontrar solução"

função obterAcoesPossiveis(estado):
    # Retorna as ações possíveis para o estado atual do quebra-cabeça
    # Exemplo de ações: 'cima', 'baixo', 'esquerda', 'direita'
    ...

função executarAcao(estado, acao):
    # Executa a ação no estado atual do quebra-cabeça e retorna o novo estado resultante
    ...

estadoInicial <- obterEstadoInicial()  # Obter o estado inicial do quebra-cabeça
estadoObjetivo <- obterEstadoObjetivo()  # Obter o estado objetivo desejado

solucao <- resolverQuebraCabeca(estadoInicial, estadoObjetivo)

se solucao != "Não foi possível encontrar solução" então:
    imprimir "Solução encontrada:"
    imprimir solucao
senão:
    imprimir "Não foi possível encontrar uma solução."
```
