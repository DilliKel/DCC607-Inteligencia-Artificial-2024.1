# Algoritmos Genéticos

Atividades práticas de resolução de problemas com algoritmos genéticos: caixeiro-viajante, N-Rainhas e mochila 0-1.

## Caixeiro Viajante

`caixeiro-viajante.ipynb` — resolve o problema do caixeiro viajante (encontrar a rota de menor custo que visita todas as cidades uma vez) usando um algoritmo genético.

## N-Rainhas

- `n-rainhas-genetico-v1.py` — primeira versão (2023.1).
- `n-rainhas-genetico-v2.ipynb` — versão aprimorada (2024.1), reescrita a partir do código de 2023 com melhorias na seleção, crossover e mutação.
- `n-rainhas-genetico-v2-conceitual.ipynb` — versão paralela de 2024.1, com uma explicação conceitual mais detalhada do esquema do algoritmo (ver abaixo).

### Esquema do algoritmo genético para N-Rainhas

O objetivo é encontrar um arranjo de N rainhas em um tabuleiro NxN em que nenhuma ataque outra (mesma linha, coluna ou diagonal).

- **Cromossomo:** vetor de genes, ex. `[1, 2, 3, 4, 5, 6, 7, 8]`, representando a linha de cada rainha (índice = coluna).
- **Gene:** posição no vetor, gerada aleatoriamente na população inicial.
- **Geração:** cada iteração de reprodução da população (`generations`).
- **Fitness:** número de pares de rainhas que se atacam (mesma linha ou diagonal). Quanto menor, melhor.
- **Seleção:** ordena a população por fitness e seleciona a proporção `best` dos indivíduos mais aptos como pais.
- **Elitismo:** o melhor cromossomo encontrado até o momento nunca é descartado, mesmo que a nova geração seja pior.
- **Crossover:** combina os genes de dois pais a partir de um ponto de corte aleatório.
- **Mutação:** troca aleatoriamente o valor de um gene, com uma pequena probabilidade (`mutation_rate`), para manter diversidade genética e evitar mínimos locais.

### Exemplos de teste (v2-conceitual)

| Teste | N rainhas | População | Gerações | Melhor fitness |
|---|---|---|---|---|
| 1 | 8 | 100 | 100 | 1 |
| 2 | 50 | 100 | 4000 | 4 |

## Mochila 0-1

Duas abordagens diferentes para o mesmo problema (2023.1):

- `mochila-0-1-genetico.ipynb` — resolve via algoritmo genético (fitness = valor total, descartando indivíduos que excedem a capacidade).
- `mochila-0-1-prog-dinamica.ipynb` — resolve via programação dinâmica bottom-up (ótimo garantido), lendo os itens de `dados-mochila.txt`.

## Enunciado

`enunciado.pdf` — descrição original da atividade prática de algoritmos genéticos.
