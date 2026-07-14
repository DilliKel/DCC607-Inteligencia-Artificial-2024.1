# Inteligência Artificial — Caderno Mestre

Resumo completo da disciplina, cobrindo fundamentos, agentes, busca, algoritmos genéticos e aprendizagem de máquina.

## Introdução

A Inteligência Artificial (IA) é um campo multidisciplinar da ciência da computação que se concentra no desenvolvimento de sistemas e algoritmos capazes de realizar tarefas que normalmente requerem inteligência humana. Essas tarefas podem incluir reconhecimento de padrões, resolução de problemas, aprendizado, tomada de decisões e processamento de linguagem natural.

### O que é IA?

IA refere-se à capacidade das máquinas de imitar ou simular características da inteligência humana. Em outras palavras, é a criação de sistemas que podem pensar, raciocinar, aprender e tomar decisões de maneira semelhante aos seres humanos. A IA envolve o desenvolvimento de algoritmos e modelos matemáticos que permitem que as máquinas processem informações e ajam de forma inteligente.

### Os fundamentos da inteligência artificial

- **Aprendizado de máquina (Machine Learning):** subcampo da IA que se concentra no desenvolvimento de algoritmos que permitem que as máquinas aprendam a partir de dados e melhorem seu desempenho ao longo do tempo, sem serem explicitamente programadas.
- **Redes neurais artificiais:** modelos matemáticos inspirados no funcionamento do cérebro humano, compostos por unidades interconectadas (neurônios artificiais) que processam e transmitem informações entre si.
- **Processamento de linguagem natural (NLP):** campo que se concentra na interação entre computadores e linguagem humana, permitindo que as máquinas entendam, interpretem e gerem linguagem natural.

### História da inteligência artificial

- **Década de 1950:** surgimento do campo da IA e desenvolvimento dos primeiros programas de IA, como o Logic Theorist e o General Problem Solver.
- **Década de 1960:** introdução da ideia de "busca heurística" para resolução de problemas complexos.
- **Década de 1970:** desenvolvimento de sistemas especialistas, programas capazes de tomar decisões em domínios específicos.
- **Década de 1980:** avanços na área de redes neurais artificiais e aprimoramento de algoritmos de aprendizado de máquina.
- **Década de 1990:** expansão da IA em diversos campos, como reconhecimento de fala, visão computacional e robótica.
- **Século XXI:** a IA se torna mais presente na sociedade, impulsionada pelo aumento da capacidade computacional, disponibilidade de grandes volumes de dados e avanços em algoritmos de aprendizado de máquina — veículos autônomos, assistentes virtuais e análise de dados.

## Algoritmo Guloso

O algoritmo guloso (voraz ou *greedy*) é uma abordagem heurística na qual uma decisão ótima é tomada em cada etapa localmente, na esperança de que isso leve a uma solução globalmente ótima. Ele toma decisões com base em uma métrica de otimalidade local, sem reconsiderar escolhas anteriores nem se preocupar com o resultado final.

O algoritmo guloso nem sempre produz uma solução globalmente ótima — em alguns casos pode levar a soluções subótimas ou incorretas.

Exemplos de problemas abordados com algoritmos gulosos:
- **Problema da mochila fracionária:** maximizar o valor total de itens em uma mochila de capacidade limitada, permitindo dividir itens em partes fracionárias.
- **Algoritmo de Kruskal** para árvore geradora mínima.
- **Algoritmo de Dijkstra** para o caminho mais curto entre um vértice de origem e todos os outros.

## Problema das N Rainhas

Desafio clássico de posicionar N rainhas em um tabuleiro NxN sem que nenhuma ameace outra (mesma linha, coluna ou diagonal). Complexidade exponencial, aproximadamente O(N!). É um problema de busca e otimização combinatória.

Abordagens:
1. **Força bruta:** gera e verifica todas as configurações possíveis. Ineficiente para N grande.
2. **Backtracking:** coloca uma rainha por coluna, verifica segurança, e retrocede quando não há posição segura, repetindo até achar uma solução válida ou esgotar as possibilidades.
3. **Algoritmo genético:** gera população de configurações aleatórias e aplica seleção, recombinação e mutação até encontrar uma configuração sem ameaças.

### Pseudocódigo (Backtracking)

```
função resolverNRainhas(N):
    solucao <- criarTabuleiroVazio(N)
    coluna <- 0

    se posicionarRainhas(solucao, coluna, N) então:
        retornar solucao
    senão:
        retornar "Não foi possível encontrar solução"

função posicionarRainhas(tabuleiro, coluna, N):
    se coluna >= N então:
        retornar verdadeiro

    para cada linha de 0 a N-1 faça:
        se éPosicaoSegura(tabuleiro, linha, coluna, N) então:
            tabuleiro[linha][coluna] <- 'Q'

            se posicionarRainhas(tabuleiro, coluna + 1, N) então:
                retornar verdadeiro

            tabuleiro[linha][coluna] <- '.'

    retornar falso

função éPosicaoSegura(tabuleiro, linha, coluna, N):
    para cada col de 0 a coluna-1 faça:
        se tabuleiro[linha][col] == 'Q' então:
            retornar falso

    i, j <- linha-1, coluna-1
    enquanto i >= 0 e j >= 0 faça:
        se tabuleiro[i][j] == 'Q' então:
            retornar falso
        i <- i-1
        j <- j-1

    i, j <- linha+1, coluna-1
    enquanto i < N e j >= 0 faça:
        se tabuleiro[i][j] == 'Q' então:
            retornar falso
        i <- i+1
        j <- j-1

    retornar verdadeiro
```

## Dijkstra

Algoritmo clássico para encontrar o caminho mais curto entre um vértice de origem e todos os outros vértices em um grafo ponderado. Amplamente usado em roteamento de redes, sistemas de navegação e otimização de caminhos.

Funcionamento:
1. Inicializa distâncias com valor infinito, exceto a origem (0).
2. Marca a origem como visitada.
3. Para cada vizinho, atualiza a distância mínima se o novo caminho for mais curto.
4. Seleciona o próximo vértice não visitado com menor distância e repete.
5. Repete até todos os vértices serem visitados ou não haver mais vértices acessíveis.

É eficiente para grafos com arestas não negativas, implementado com uma fila de prioridade.

```
função dijkstra(grafo, inicio):
    distancias <- inicializarDistancias(inicio)
    visitados <- criarConjuntoVazio()
    filaPrioridade <- criarFilaPrioridade()

    adicionarNaFilaPrioridade(filaPrioridade, (inicio, 0))

    enquanto não vazio(filaPrioridade) faça:
        no, distancia <- removerDaFilaPrioridade(filaPrioridade)
        adicionar em visitados

        para cada vizinho, peso em obterVizinhos(grafo, no) faça:
            novaDistancia <- distancia + peso

            se novaDistancia < distancias[vizinho] então:
                distancias[vizinho] <- novaDistancia
                adicionarNaFilaPrioridade(filaPrioridade, (vizinho, novaDistancia))

    retornar distancias
```

## Agentes e Ambientes

Um agente é tudo que pode ser considerado capaz de perceber seu ambiente por meio de sensores e de agir sobre esse ambiente por intermédio de atuadores.

**Agindo de forma humana: teste de Turing**
- *Percepção*: entradas perceptivas do agente em um dado instante.
- *Sequência de percepções*: história completa de tudo o que o agente já percebeu.
- O comportamento do agente é descrito pela **função do agente**, que mapeia qualquer sequência de percepções para uma ação. Internamente, ela é implementada pelo **programa do agente**.

**O mundo do aspirador de pó** — exemplo clássico: o agente percebe se a célula está suja ou limpa e decide mover-se ou limpar.

### Racionalidade

Um agente é racional quando toma ações que maximizam suas chances de alcançar seus objetivos, considerando seu conhecimento e percepção do ambiente. Depende de quatro fatores:
- A medida de desempenho que define o critério de sucesso.
- O conhecimento prévio que o agente tem do ambiente.
- As ações que o agente pode executar.
- A sequência de percepções do agente até o momento.

**Definição de agente racional:** para cada sequência de percepções possível, um agente racional deve selecionar uma ação que se espera venha a maximizar sua medida de desempenho, dada a evidência da sequência de percepções e qualquer conhecimento interno do agente.

### Onisciência

Um agente onisciente tem conhecimento completo e preciso do ambiente — mas isso é impossível na realidade. Racionalidade maximiza o desempenho *esperado*; perfeição maximizaria o desempenho *real*. Não são a mesma coisa.

### Especificando o ambiente de tarefa — PEAS

**PEAS** (Performance, Environment, Actuators, Sensors — desempenho, ambiente, atuadores, sensores) é usado para especificar o ambiente de tarefa de um agente.

### Propriedades de ambientes de tarefas

- **Completamente observável vs parcialmente observável:** o agente tem acesso a todas as informações relevantes vs. apenas a uma parte, sujeitas a ruído.
- **Agente único vs multiagente:** um agente sozinho (ex.: palavras cruzadas) vs. vários agentes interagindo (ex.: xadrez).
- **Determinístico vs estocástico:** o próximo estado é completamente determinado pelo estado atual e pela ação vs. envolve incerteza.
- **Episódico vs sequencial:** cada episódio é independente vs. ações afetam episódios subsequentes.
- **Estático vs dinâmico:** o ambiente não muda enquanto o agente delibera vs. pode mudar independentemente.
- **Contínuo vs discreto:** ações e percepções em espaço contínuo vs. conjunto finito de opções.

### Estrutura dos agentes

**AGENTE = ARQUITETURA + PROGRAMA**

O programa do agente implementa a função do agente, executado em um dispositivo com sensores e atuadores físicos (arquitetura).

Tipos básicos de programas de agentes:
- **Reativos simples:** decidem apenas com base nas percepções atuais, via regras estímulo-resposta. Adequados a ambientes simples.
- **Reativos baseados em modelos:** mantêm um modelo interno do ambiente, permitindo antecipar mudanças e agir em situações não previamente encontradas.
- **Baseados em objetivos:** consideram objetivos de longo prazo, usando informações passadas e planejamento.
- **Baseados em utilidade:** avaliam a utilidade/desejabilidade das ações, escolhendo a de maior utilidade esperada.
- **Com aprendizagem:** melhoram o desempenho ao longo do tempo por meio da experiência.

## Agentes de Resolução de Problemas

Programas de agentes que analisam o estado atual, identificam o objetivo e tomam ações para alcançá-lo, seguindo formulação do problema → geração de soluções → avaliação.

Técnicas comuns:
- **Busca em espaço de estados:** busca em largura, profundidade, custo uniforme, heurística.
- **Algoritmos de otimização:** algoritmos genéticos, evolutivos, enxame de partículas.
- **Sistemas especialistas:** baseados em regras/conhecimento especializado.
- **Raciocínio baseado em casos:** adapta soluções de casos passados semelhantes.

## Mapa da Romênia

Problema clássico de busca de caminho em um grafo: encontrar o caminho mais curto entre duas cidades da Romênia, dado um mapa com estradas e distâncias associadas.

**Atividade II — A\*:** implementar o Algoritmo A Estrela capaz de resolver o problema do Mapa da Romênia e problemas da mesma classe.

### Pseudocódigo do A*

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

            novo_g = g[u] + custo(u, v)
            se v não está em lista_aberta ou novo_g < g[v]:
                g[v] = novo_g
                f[v] = g[v] + h(v, alvo)
                se v não está em lista_aberta, então
                    adicione v em lista_aberta

    retorne "Caminho não encontrado"
```

## Quebra-Cabeça de Oito Peças (8-Puzzle)

Tabuleiro 3x3 com 8 peças numeradas e uma célula vazia. Objetivo: rearranjar as peças até a configuração final (geralmente ordem numérica crescente), movendo-as uma de cada vez.

Pode ser resolvido com busca em largura, profundidade ou busca heurística. Uma heurística comum é a **distância de Manhattan**, que soma as distâncias horizontais e verticais entre cada peça e sua posição final.

### Pseudocódigo do 8-Puzzle (BFS)

```
função resolverQuebraCabeca(estadoInicial, estadoObjetivo):
    fila <- criarFila()
    visitados <- criarConjuntoVazio()

    adicionarNaFila(fila, (estadoInicial, []))

    enquanto não vazio(fila) faça:
        estado, acoes <- removerDaFila(fila)

        se estado == estadoObjetivo então:
            retornar acoes

        adicionar estado em visitados

        para cada acao em obterAcoesPossiveis(estado) faça:
            novoEstado <- executarAcao(estado, acao)

            se novoEstado não está em visitados então:
                adicionarNaFila(fila, (novoEstado, acoes + [acao]))

    retornar "Não foi possível encontrar solução"
```

## Medição de Desempenho de Resolução de Problemas

Quatro aspectos avaliados:
- **Completeza:** o algoritmo garante encontrar uma solução quando ela existir?
- **Otimização:** a estratégia encontra a solução ótima?
- **Complexidade de tempo:** quanto tempo leva para encontrar uma solução?
- **Complexidade de espaço:** quanta memória é necessária?

## Infraestrutura para Algoritmos de Busca

Componentes-chave de um nó da árvore de busca:
- **Estado (n.ESTADO):** representação do estado no espaço de estado.
- **Pai (n.PAI):** nó que gerou o nó atual, usado para reconstruir o caminho.
- **Ação (n.AÇÃO):** ação aplicada ao pai para gerar o nó atual.
- **Custo do caminho (n.CUSTO-DO-CAMINHO):** custo g(n) do caminho do estado inicial até o nó atual.

## Estratégias de Busca Não Informada

### Busca em Largura (BFS)

Explora os nós em camadas, expandindo todos os vizinhos antes de avançar. Garante o caminho mais curto, mas pode consumir muita memória.

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

### Busca de Custo Uniforme

Expande os nós com o menor custo de caminho acumulado, usando uma fila de prioridade. Encontra o caminho mais barato desde que os custos sejam não negativos.

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

### Busca em Profundidade (DFS)

Explora um ramo até o limite antes de retroceder. Eficiente em memória (não requer armazenar toda a árvore), mas pode não achar o caminho mais curto e pode entrar em loop em grafos com ciclos.

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

### Busca em Profundidade Limitada

Variação da DFS com um limite máximo de profundidade. Evita exploração excessiva em ramos profundos, mas pode falhar se a solução estiver além do limite.

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

### Busca de Aprofundamento Iterativo (IDDFS)

Combina a busca em profundidade com aumentos progressivos do limite. Mantém a eficiência de memória da DFS e pode encontrar soluções ótimas como a BFS.

```
busca_de_aprofundamento_iterativo(inicio, objetivo):
    limite = 0

    enquanto verdadeiro:
        resultado = busca_em_profundidade_limitada(inicio, objetivo, limite)

        se resultado ≠ "Limite de profundidade atingido":
            retorne resultado

        limite += 1
```

### Explorar Nodos

Explorar nós significa visitar/examinar os nós do espaço de busca em determinada ordem, aplicando ações para avançar de um estado para outro, verificando se é o objetivo, se já foi visitado, e se é válido segundo as restrições do problema. A estratégia de exploração escolhida afeta diretamente eficiência, completude e otimalidade do algoritmo.

## Algoritmos Genéticos

Técnica de otimização e busca inspirada na evolução biológica, usada para encontrar soluções aproximadas ou ótimas em espaços de busca grandes e multidimensionais.

Conceitos básicos:
1. **População:** conjunto de indivíduos, cada um uma possível solução.
2. **Codificação:** representação manipulável do indivíduo (comumente binária).
3. **Função de aptidão (fitness):** pontua a qualidade de cada indivíduo.
4. **Seleção:** indivíduos com maior aptidão têm mais chance de reprodução (roleta, torneio, classificação).
5. **Reprodução:** cruzamento (recombinação) e mutação (variação aleatória) geram novos indivíduos.
6. **Evolução:** repete seleção, reprodução e evolução por várias gerações até uma condição de parada.
7. **Convergência:** indivíduos mais aptos tendem a dominar a população.

### TPOT (Tree-Based Pipeline Optimization Tool)

Ferramenta de AutoML que usa programação genética para otimizar pipelines de machine learning (pré-processamento + modelo), aplicando mutação, recombinação e seleção sobre uma população de pipelines, avaliados por uma métrica de desempenho (acurácia, precisão, recall, F1). Reduz a necessidade de ajuste manual, mas não substitui o conhecimento especializado na interpretação dos resultados.

## Aprendizagem de Máquina (Machine Learning)

Subárea da IA que desenvolve algoritmos que aprendem a partir de dados e melhoram o desempenho em tarefas específicas sem serem explicitamente programados. *"Não preciso dizer o que ele tem que fazer, só preciso mostrar vários exemplos de COMO fazer!"*

### Exemplo do Filtro de Spam

Primeira aplicação de aprendizagem de sucesso (anos 90): rotula e-mails como spam/ham a partir de exemplos rotulados.
- **Conjunto de treinamento:** exemplos usados para aprender.
- **Conjunto de teste:** usado para medir o desempenho.
- **Instância:** cada exemplo na base de dados.
- Tarefa T = rotular e-mails; Experiência E = conjunto de treinamento; Métrica de desempenho P = proporção de instâncias corretamente classificadas.

### Por que utilizar Aprendizagem de Máquina?

1. Lidar com dados complexos e volumosos.
2. Adaptabilidade a novos dados e mudanças no ambiente.
3. Automação e eficiência de tarefas repetitivas.
4. Tomada de decisões inteligentes com base em padrões identificados.

### Tipos de Aprendizagem de Máquina

1. **Supervisionada:** treinada em dados rotulados.
   - **Regressão:** prevê valor numérico contínuo (ex.: preço de imóveis).
   - **Classificação:** atribui categorias/rótulos (ex.: spam ou não spam).
2. **Não supervisionada:** dados não rotulados.
   - **Clustering:** identifica padrões/grupos.
   - **Associação:** descobre relações entre itens.
   - **Detecção de anomalias:** identifica desvios do padrão geral.
3. **Aprendizagem por reforço:** agente aprende ações que maximizam recompensa por meio de feedback do ambiente.
4. **Semi-supervisionada:** combina dados rotulados (limitados) e não rotulados para melhorar a precisão.
5. **Aprendizagem em batch:** treina com todo o conjunto de dados de uma vez; adequada a conjuntos menores.
6. **Aprendizagem online:** modelo atualizado continuamente à medida que novos dados chegam, adequado a fluxo contínuo de dados.

### Treinamento com Labels (rótulos)

Conjunto de dados onde cada exemplo está associado a um rótulo/classe correspondente, essencial na aprendizagem supervisionada para que o modelo aprenda a mapear entradas para saídas corretas.

### Instance-based vs Model-based

- **Instance-based:** usa medida de similaridade para generalizar a partir de exemplos armazenados (ex.: k-Nearest Neighbors).
- **Model-based:** constrói um modelo explícito que descreve a relação entre entradas e saída (ex.: regressão linear, árvores de decisão, redes neurais).

### Problemas de Aprendizagem de Máquina

Reconhecimento de voz, sistemas de recomendação, reconhecimento de objetos em imagens, detecção de fraude, segmentação de clientes, processamento de linguagem natural, detecção de spam, previsão de demanda, diagnóstico médico, reconhecimento facial, previsão de preço imobiliário.

### Pipeline de Aprendizado de Máquina

1. Coleta e pré-processamento dos dados (limpeza, valores ausentes, normalização, codificação).
2. Seleção e extração de recursos (análise exploratória, PCA).
3. Escolha do modelo e treinamento (otimização de parâmetros).
4. Avaliação do modelo (métricas em dados de teste).
5. Implantação do modelo em produção.

### Principais Desafios de AM

1. **Quantidade insuficiente de dados de treinamento** — problemas complexos podem exigir milhões de amostras.
2. **Dados não representativos** — o modelo pode não generalizar bem.
3. **Dados com baixa qualidade** — erros e ruídos levam a resultados imprecisos.
4. **Atributos irrelevantes** — prejudicam o desempenho e introduzem ruído.
5. **Overfitting** — modelo memoriza os dados de treino em vez de generalizar.
6. **Underfitting** — modelo simples demais para capturar a complexidade dos dados.

### Dilema Viés-Variância

- **Viés (bias):** suposições simplificadoras do modelo; alto viés → underfitting.
- **Variância:** sensibilidade a flutuações nos dados de treino; alta variância → overfitting.
- O objetivo é equilibrar viés e variância para um modelo que generalize bem — reduzir um tende a aumentar o outro.

### Tendências em Aprendizagem de Máquina

1. Interpretabilidade e transparência de modelos.
2. Aprendizado profundo (Deep Learning) com redes neurais profundas.
3. Aprendizado de máquina federado (treino distribuído preservando privacidade).
4. Aprendizado ativo (o modelo seleciona quais instâncias devem ser rotuladas).

## Métricas de Avaliação

### Revocação (Recall)

Proporção de exemplos positivos corretamente identificados em relação ao total de positivos existentes.

```
Revocação = Verdadeiros Positivos / (Verdadeiros Positivos + Falsos Negativos)
```

Exemplo: VP=80, FN=20 → Revocação = 80/100 = 80%. Importante quando é crucial não deixar passar casos positivos (ex.: diagnóstico médico).

### Precisão

Proporção de exemplos classificados como positivos que realmente são positivos.

```
Precisão = Verdadeiros Positivos / (Verdadeiros Positivos + Falsos Positivos)
```

Exemplo: VP=80, FP=10 → Precisão = 80/90 ≈ 88,88%. Importante quando é crucial evitar falsos positivos (ex.: filtro de spam não bloquear e-mails legítimos).

Precisão e revocação são complementares — aumentar uma tende a diminuir a outra. A **medida F1** (média harmônica de precisão e revocação) combina as duas em uma única métrica balanceada.

> O que conta como "bom resultado" depende do problema: 88,88% de precisão e 80% de revocação podem ser ótimos para classificar galáxias, mas insuficientes para diagnosticar câncer de mama, onde falsos negativos têm consequências graves.

### Acurácia

Proporção de instâncias corretamente classificadas em relação ao total avaliado. Pode ser enganosa em problemas desbalanceados, quando precisão e recall dão uma visão mais completa.

### Outras Métricas

- **F1-score:** média harmônica entre precisão e recall.
- **Matriz de Confusão:** tabela que compara predições com rótulos reais.
- **Curva ROC:** taxa de verdadeiros positivos vs. taxa de falsos positivos em diferentes limiares de classificação.

## Regressão Polinomial e Logística

- **Regressão Polinomial:** ajusta uma curva polinomial (em vez de reta) entre variáveis, capturando relações não lineares.
- **Regressão Logística:** algoritmo para classificação binária que aplica uma função sigmoidal para gerar a probabilidade de uma instância pertencer a uma classe. Usado em detecção de spam, diagnóstico médico, risco de crédito.

## Softmax

Função de ativação usada em classificação multiclasse: converte as saídas de um modelo em probabilidades que somam 1. Comum em redes neurais para classificação com mais de duas classes.

## Otimização por Colônia de Formigas (ACO)

Meta-heurística inspirada no comportamento de formigas reais, que depositam feromônio nas trilhas mais curtas até a comida. Aplicações: roteamento de internet, sistemas de GPS, detecção de bordas em imagens.

O algoritmo genético e o ACO foram temas do projeto final da disciplina em 2023.1 (ver [`projeto-final/2023-colonia-de-formigas`](../projeto-final/2023-colonia-de-formigas/)).

## Redes Neurais

Método de IA que ensina computadores a processar dados de forma inspirada no cérebro humano, usando nós (neurônios/perceptrons) interconectados em camadas. É a base do aprendizado profundo (deep learning).

- Quanto mais neurônios, melhor a capacidade — mas maior o risco de overfitting, exigindo mais regularização.
- Casos de uso: diagnóstico médico, marketing direcionado, previsões financeiras, previsão de demanda de energia, controle de qualidade, identificação de compostos químicos.

### Tipos de Redes Neurais

- **Feedforward:** dados fluem em uma direção, do nó de entrada ao de saída.
- **Backpropagation:** algoritmo de aprendizado contínuo por feedback corretivo — os nós ajustam pesos dos caminhos conforme a precisão dos palpites.
- **Convolucionais (CNN):** camadas ocultas aplicam convoluções (filtragem, resumo), muito úteis para classificação de imagens, extraindo bordas, cores e profundidade em cada camada.

## Referências

- Russell & Norvig — *Inteligência Artificial* (livro-texto de resolução de problemas por meio de busca).
- Repositório da disciplina em 2023.1: [github.com/DilliKel/DCC607-Inteligencia-Artificial-2023.1](https://github.com/DilliKel/DCC607-Inteligencia-Artificial-2023.1)
- "The Elements of Statistical Learning" — Hastie, Tibshirani, Friedman.
- "Pattern Recognition and Machine Learning" — Christopher Bishop.
- "Deep Learning" — Ian Goodfellow, Yoshua Bengio, Aaron Courville.
- Curso "Machine Learning" — Andrew Ng (Coursera / Stanford OpenClassroom).
- Journal of Machine Learning Research — jmlr.org
