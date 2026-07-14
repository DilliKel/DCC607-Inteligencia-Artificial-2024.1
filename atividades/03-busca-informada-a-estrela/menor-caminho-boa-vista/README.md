# Menor Caminho em Boa Vista/RR — OSMnx + A*

Aplicação do algoritmo A* sobre um grafo de ruas real, extraído do OpenStreetMap com a biblioteca [OSMnx](https://osmnx.readthedocs.io/), para calcular o menor caminho entre dois pontos de Boa Vista, capital de Roraima.

## Como funciona

1. Baixa o grafo viário de uma região de Boa Vista a partir de um ponto central (latitude/longitude) e um raio de busca, usando `ox.graph_from_point(...)`.
2. Plota o grafo das ruas baixado com `ox.plot_graph(G)`.
3. Define origem e destino (ex.: "Casita" → "Bloco 5") a partir de coordenadas reais.
4. Encontra os nós do grafo mais próximos da origem e do destino com `ox.distance.nearest_nodes`.
5. Calcula o menor caminho entre os dois nós.

## Requisitos

- `osmnx`
- `networkx`
- `matplotlib`

## Como executar

Abra `MenorCaminhoCCT.ipynb` no Jupyter e execute as células em ordem — a primeira célula baixa o grafo da região via internet (OpenStreetMap), então é necessário estar conectado.
