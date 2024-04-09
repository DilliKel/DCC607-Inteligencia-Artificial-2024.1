# Relatório sobre a Aplicação do Algoritmo A* para Encontrar o Menor Caminho da minha casa até o Bloco V, CCT

---
Kelvin Araújo Ferreira - 2019037653

---

## Introdução:

Este relatório descreve a abordagem adotada para aplicar o algoritmo A* com o objetivo de encontrar o menor caminho até o Bloco V, CCT, utilizando as bibliotecas NetworkX, Matplotlib e OSMnx. O algoritmo A* é uma técnica eficaz para encontrar o caminho mais curto entre dois pontos em um grafo ponderado, considerando tanto o custo do movimento quanto uma heurística que estima o custo restante até o destino.

---

## Descrição da Abordagem:

1. **Obtenção dos Dados Geográficos:**
   - As coordenadas geográficas da cidade foram especificadas através do Google Maps, definindo o centro da área de interesse.
   - Um raio de busca foi definido para limitar a área de interesse ao redor do centro especificado, neste caso foi do Blodo 5 da UFRR.
   - Utilizando a biblioteca OSMnx, foi baixado o grafo de ruas da região dentro do raio especificado, considerando apenas as vias para veículos.

2. **Definição das Origem e Destino:**
   - A origem foi definida como as coordenadas da "Casa".
   - O destino foi definido como as coordenadas do "Bloco V, CCT".

3. **Encontrando os Nós Mais Próximos:**
   - Utilizando a função `nearest_nodes` da biblioteca OSMnx, os nós mais próximos no grafo foram identificados para as coordenadas de origem e destino.

4. **Aplicação do Algoritmo A*:**
   - Utilizando a biblioteca NetworkX, o algoritmo A* foi aplicado para encontrar o menor caminho entre os nós de origem e destino no grafo.
   - O peso considerado para calcular o caminho mais curto foi o comprimento das arestas do grafo, representando a distância entre os pontos.

5. **Visualização dos Resultados:**
   - O menor caminho encontrado foi plotado sobre o grafo de ruas para visualização.
   - O caminho foi destacado em um gráfico, enquanto os nós e as arestas foram ocultados para maior clareza.

---

## Resultados Obtidos:

O menor caminho encontrado entre a origem (Casa) e o destino (Bloco V, CCT) é representado por uma série de segmentos de ruas, conforme visualizado no gráfico.

---

## Análise dos Resultados:

A aplicação do algoritmo A* mostrou-se eficaz na identificação do menor caminho entre a origem e o destino no grafo de ruas da cidade. A rota resultante parece ser uma escolha razoável, considerando o critério de distância. No entanto, é importante notar que o menor caminho pode não ser o mais rápido em termos de tempo de viagem, uma vez que fatores como tráfego e restrições de direção não são considerados nesta abordagem. Portanto, para uma aplicação prática, podem ser necessárias considerações adicionais.

Matematicamente dizemos que o menor caminho entre dois pontos, é uma linha reta. Neste caso traçar uma linha reta ou fazer várias curvas em direção ao destino seria a melhor escolha. Porém matematicamente falando, quanto mais curvas mais longe seria. Então durante os nossos testes, testamos vários locais e em todos eles foram traçados o máximo de linhas retas possíveis.

---

## Conclusão:

A utilização do algoritmo A* em conjunto com as bibliotecas Python NetworkX, Matplotlib e OSMnx permitiu encontrar de forma eficiente o menor caminho entre a origem (Casa) e o destino (Bloco V, CCT) dentro da cidade. Este relatório fornece uma visão geral da abordagem adotada, dos resultados obtidos e de uma análise crítica desses resultados.

---

### Informações Adicionais:

- As coordenadas geográficas para os endereços são:
  - **Casa (Rua Linha Fina, 441, Jóquei Clube, Boa Vista - RR, 69313-038):**
    - Latitude: 2.806972
    - Longitude: -60.717536
  - **Bloco V (Av. Cap. Ene Garcês, 2413, Bloco V, Aeroporto, Boa Vista - RR, 69310-000):**
    - Latitude: 2.835091
    - Longitude: -60.694924

- Documentação da biblioteca OSMnx: [Link](https://osmnx.readthedocs.io/)
- Documentação da biblioteca NetworkX: [Link](https://networkx.org/documentation/)
- Documentação da API do Google Maps: [Link](https://developers.google.com/maps/documentation)
- Livro: "Artificial Intelligence: A Modern Approach" de Stuart Russell e Peter Norvig (Capítulo 3).

