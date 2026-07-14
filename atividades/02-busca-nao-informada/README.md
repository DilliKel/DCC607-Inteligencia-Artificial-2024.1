# Busca Não Informada — 8-Puzzle

Duas abordagens diferentes para resolver o quebra-cabeça de 8 peças (8-puzzle), desenvolvidas em 2024.1.

## `8-puzzle-busca-aleatoria.ipynb`

Busca aleatória: a cada passo, um movimento válido é escolhido aleatoriamente entre os vizinhos da posição vazia (cima, baixo, esquerda, direita), até encontrar o estado objetivo ou atingir um limite de iterações (100.000). É a abordagem mais simples de busca não informada — não usa nenhuma heurística nem histórico, apenas tentativa e erro.

## `8-puzzle-algoritmo-genetico.ipynb`

Versão avulsa que resolve o mesmo problema com um algoritmo genético: gera uma população de tabuleiros embaralhados, avalia cada um pelo número de peças fora do lugar (fitness) e evolui a população por seleção, crossover e mutação até minimizar o fitness. Incluído aqui porque resolve o mesmo problema do 8-puzzle, ainda que a técnica (busca evolutiva) seja mais próxima do conteúdo de [algoritmos genéticos](../04-algoritmos-geneticos/).

> Nota: o problema das N-Rainhas também foi resolvido nesta disciplina, mas usando algoritmo genético — por isso está documentado em [`04-algoritmos-geneticos/`](../04-algoritmos-geneticos/) em vez desta pasta.
