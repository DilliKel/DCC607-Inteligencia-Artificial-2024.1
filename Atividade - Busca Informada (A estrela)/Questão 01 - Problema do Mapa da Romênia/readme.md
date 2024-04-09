# Relatório sobre a Implementação do Algoritmo A* para o Problema do Mapa da Romênia

---
Kelvin Araújo Ferreira - 2019037653

---

## Introdução:

Este relatório descreve a abordagem adotada para implementar o algoritmo A* para resolver o problema do mapa da Romênia. O objetivo é encontrar o menor caminho entre duas cidades, utilizando um grafo representando as conexões entre as cidades e uma heurística para orientar a busca.

---

## Representação do Mapa da Romênia:

O mapa da Romênia é representado como um grafo, onde cada cidade é um nó e as estradas entre as cidades são as arestas. O grafo é implementado como um dicionário em Python, onde as chaves são os nomes das cidades e os valores são outros dicionários, representando as conexões de cada cidade com suas vizinhas e os custos associados a essas conexões.

---

## Heurística Escolhida:

Para orientar a busca do algoritmo A*, foi escolhida uma heurística baseada na distância estimada entre cada cidade e o destino final (Bucharest). Essa heurística é armazenada em um dicionário, onde as chaves são os nomes das cidades e os valores são as distâncias estimadas até Bucharest.

---

## Abordagem para a Implementação do Algoritmo A*:

1. **Função de Heurística:**
   - Uma função de heurística foi definida para calcular a estimativa do custo restante de cada nó até o destino final.

2. **Algoritmo A*:**
   - O algoritmo A* foi implementado para encontrar o menor caminho entre duas cidades no mapa da Romênia.
   - A fila de prioridade foi utilizada para garantir que os nós com menor custo total fossem explorados primeiro.
   - Durante a busca, o custo atual do caminho percorrido até cada nó foi armazenado.

3. **Leitura dos Dados:**
   - Os dados do mapa da Romênia e da heurística foram lidos a partir de arquivos de texto.

4. **Execução do Algoritmo:**
   - O algoritmo A* foi executado para encontrar o menor caminho entre a cidade de partida (Arad) e a cidade de destino (Bucharest).

---

## Resultados Obtidos:

O algoritmo A* foi capaz de encontrar o menor caminho entre a cidade de partida (Arad) e a cidade de destino (Bucharest). O caminho encontrado foi exibido no console, juntamente com o custo total do caminho. Os resultados obtidos foram satisfatórios e condizentes com as expectativas.

---

## Discussão dos Resultados:

Em cada caso de teste, o algoritmo A* encontrou o menor caminho esperado, conforme determinado pelo mapa da Romênia e pela heurística utilizada. A implementação demonstrou eficiência em encontrar o caminho mais curto entre as cidades, graças à combinação da heurística admissível com a busca informada pelo algoritmo A*.

---

## Conclusão:

A implementação do algoritmo A* para resolver o problema do mapa da Romênia foi bem-sucedida. O algoritmo foi capaz de encontrar o menor caminho entre duas cidades de forma eficiente e precisa, garantindo resultados confiáveis. Este relatório fornece uma visão geral da abordagem adotada, dos resultados obtidos e de uma discussão sobre esses resultados.
