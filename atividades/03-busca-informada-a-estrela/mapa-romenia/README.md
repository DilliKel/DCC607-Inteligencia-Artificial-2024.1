# Mapa da Romênia — Busca A*

Implementação clássica do algoritmo A* (A Estrela) aplicado ao problema do Mapa da Romênia, exemplo canônico do livro *Artificial Intelligence: A Modern Approach* (Russell & Norvig).

## Problema

Encontrar o menor caminho entre duas cidades da Romênia, dado um grafo de estradas com distâncias reais entre cidades vizinhas (`Romenia.txt`) e uma heurística de distância em linha reta até o destino (`Heuristica.txt`), usada para guiar a busca.

## Arquivos

- `A_Estrela-Romenia.py` — implementação do algoritmo A*, que combina o custo do caminho percorrido (g) com a heurística até o objetivo (h) para escolher o próximo nó a expandir.
- `Romenia.txt` — grafo de adjacência das cidades e distâncias entre elas.
- `Heuristica.txt` — valores heurísticos (distância em linha reta) de cada cidade até o destino.
- `mapa-da-romenia.png` — mapa de referência com as cidades e estradas do problema.

## Como executar

```bash
python A_Estrela-Romenia.py
```
