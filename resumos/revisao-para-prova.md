# Revisão para a Prova

Perguntas e respostas de revisão, cobrindo aprendizagem de máquina, busca e algoritmos genéticos.

> As respostas marcadas com "R:" vieram do material original do Notion. As perguntas que o material original deixava sem resposta (autoestudo antes da prova) foram respondidas aqui com base no [caderno mestre de IA](./caderno-mestre-ia.md) e conhecimento padrão da área — marcadas como *(resposta complementar)*.

**Quais são os principais desafios da aprendizagem de máquina?**
R: Quantidade insuficiente de dados de treinamento, dados não representativos, dados com baixa qualidade, atributos irrelevantes, overfitting, underfitting.

**Quais são os principais problemas da aprendizagem de máquina?**
R: Reconhecimento de voz, reconhecimento de objetos em imagens, detecção de fraude, detecção de spam, reconhecimento facial.

**Como podemos lidar com o problema do overfitting em um modelo preditivo?**
R: Regularização, aumento de dados (data augmentation), validação cruzada (cross-validation), redução de dimensionalidade, aumento cuidadoso da complexidade do modelo, aumento do tamanho do conjunto de treinamento.

**Quais são os diferentes tipos de algoritmos de aprendizagem de máquina supervisionada?**
R: Regressão e classificação.

**Explique a diferença entre aprendizagem supervisionada e aprendizagem não supervisionada.**
R: Na aprendizagem supervisionada o algoritmo é treinado em dados rotulados, onde as entradas estão associadas a rótulos ou resultados conhecidos, e o objetivo é aprender a mapear entradas para saídas corretas. Na aprendizagem não supervisionada o algoritmo recebe dados não rotulados e busca encontrar padrões, estruturas ou agrupamentos, sem necessidade de rótulos prévios.

**Qual é o objetivo do conjunto de validação em um processo de treinamento de modelo?**
R: Avaliar o desempenho do modelo em dados não vistos durante o treinamento, estimando como ele se sairá em novos exemplos e apoiando decisões como seleção de hiperparâmetros e detecção de overfitting, garantindo uma avaliação imparcial e capacidade de generalização.

**Como o dilema viés-variância está relacionado ao overfitting e underfitting?**
R: O dilema viés-variância descreve o trade-off entre a capacidade do modelo de aprender padrões complexos (baixo viés) e sua sensibilidade excessiva aos dados de treinamento (alta variância). Overfitting ocorre com alta variância (ajusta-se demais ao treino, generaliza mal); underfitting ocorre com alto viés (modelo simples demais, não captura os padrões relevantes). O objetivo é equilibrar viés e variância para um modelo que generalize bem.

**Quais são as principais métricas de avaliação utilizadas na aprendizagem de máquina?**
R: Acurácia, precisão, recall (revocação), F1-score, matriz de confusão, curva ROC.

**Como o algoritmo de K-means funciona na clusterização de dados?** *(resposta complementar)*
R: K-means particiona os dados em K clusters. Primeiro escolhe K centroides iniciais (aleatórios ou por alguma heurística), atribui cada ponto ao centroide mais próximo, recalcula cada centroide como a média dos pontos atribuídos a ele, e repete a atribuição/recálculo até os centroides pararem de mudar (convergência) ou um número máximo de iterações ser atingido.

**Descreva o processo de segmentação de consumidores em múltiplos grupos usando algoritmos de aprendizagem de máquina.** *(resposta complementar)*
R: Aplica-se aprendizagem não supervisionada (tipicamente K-means ou clustering hierárquico) sobre atributos dos consumidores — comportamento de compra, dados demográficos, preferências — para agrupar clientes com perfis semelhantes em clusters distintos. Cada grupo resultante pode então receber estratégias de marketing e comunicação direcionadas ao seu perfil.

**Como a aprendizagem baseada em instância usa uma métrica de similaridade para fazer previsões?** *(resposta complementar)*
R: Em vez de construir um modelo explícito durante o treinamento, o algoritmo armazena as instâncias de treinamento. Para prever uma nova instância, ele calcula uma métrica de similaridade (ex.: distância euclidiana) entre ela e as instâncias armazenadas, e usa as *k* mais similares (k-Nearest Neighbors) para decidir a predição — por votação da classe majoritária (classificação) ou média dos valores (regressão).

**Como você lidaria com o problema de dados não representativos em um conjunto de treinamento?** *(resposta complementar)*
R: Coletando mais dados que cubram os cenários e variações faltantes, usando amostragem estratificada para garantir que todas as subpopulações relevantes estejam representadas, aplicando técnicas de balanceamento/reamostragem quando há desbalanceamento de classes, e validando o modelo em dados de fontes ou períodos diferentes dos usados no treinamento.

**Quais são os passos típicos em um pipeline de aprendizagem de máquina?** *(resposta complementar)*
R: (1) Coleta e pré-processamento dos dados; (2) seleção e extração de recursos/atributos; (3) escolha do modelo e treinamento; (4) avaliação do modelo em dados de teste; (5) implantação do modelo em produção. Ver detalhes no [caderno mestre de IA](./caderno-mestre-ia.md#pipeline-de-aprendizado-de-máquina).

**Explique a diferença entre acurácia e precisão em termos de métricas de avaliação.** *(resposta complementar)*
R: Acurácia é a proporção de todas as instâncias corretamente classificadas (positivas e negativas) em relação ao total. Precisão é a proporção de instâncias classificadas como positivas que são *realmente* positivas (VP / (VP + FP)). Acurácia pode ser enganosa em conjuntos desbalanceados, enquanto precisão foca especificamente na confiabilidade das predições positivas.

**Quais são os principais desafios ao lidar com conjuntos de dados desbalanceados em aprendizagem de máquina?**
R: Viés na predição, avaliação inadequada do desempenho, risco de overfitting, dificuldade na captura de padrões das classes minoritárias e necessidade de técnicas de amostragem e ajuste de pesos. É importante usar métricas adequadas (precisão e recall) e técnicas como reamostragem e ajuste de pesos para equilibrar as classes.

**Como a técnica de validação cruzada pode ser usada para avaliar o desempenho do modelo?** *(resposta complementar)*
R: O conjunto de dados é dividido em *k* partes (folds). O modelo é treinado em *k-1* folds e testado no fold restante; esse processo se repete *k* vezes, alternando qual fold é usado para teste. A média das métricas obtidas nas *k* rodadas dá uma estimativa mais robusta e menos dependente de uma única divisão treino/teste.

**Descreva a diferença entre regressão polinomial e regressão linear simples.** *(resposta complementar)*
R: A regressão linear simples ajusta uma reta que relaciona uma variável independente à variável dependente, assumindo relação linear. A regressão polinomial ajusta uma curva de grau superior (quadrática, cúbica, etc.), permitindo capturar relações não lineares entre as variáveis — mas com maior risco de overfitting se o grau escolhido for alto demais para a quantidade de dados disponível.

**Quais são as etapas envolvidas no pré-processamento de dados antes de aplicar algoritmos de aprendizagem de máquina?** *(resposta complementar)*
R: Limpeza de dados (tratamento de valores ausentes e duplicados), tratamento de outliers, normalização/padronização de escalas, codificação de variáveis categóricas (ex.: one-hot encoding), divisão em conjuntos de treino/validação/teste, e seleção dos atributos relevantes para o problema.

**Explique o conceito de regularização em aprendizagem de máquina e como ela pode ajudar a evitar o overfitting.** *(resposta complementar)*
R: Regularização adiciona uma penalidade à função de custo do modelo relacionada à magnitude dos seus parâmetros (ex.: L1/Lasso soma os valores absolutos dos pesos, L2/Ridge soma os quadrados). Isso desencoraja pesos muito grandes, reduzindo a complexidade efetiva do modelo e sua tendência a memorizar ruído dos dados de treino — o que melhora a generalização e reduz o overfitting.

**Quais são os principais desafios ao treinar um modelo de aprendizagem profunda?** *(resposta complementar)*
R: Necessidade de grandes volumes de dados rotulados, alto custo computacional (geralmente exigindo GPUs), risco elevado de overfitting em redes com muitos parâmetros, dificuldade de interpretar as decisões do modelo (problema de "caixa-preta"), grande número de hiperparâmetros a ajustar, e problemas de otimização como o gradiente que desaparece (*vanishing gradient*) em redes muito profundas.

**Como os algoritmos genéticos podem ser aplicados em problemas de otimização?** *(resposta complementar)*
R: Cada solução candidata é codificada como um "cromossomo". Uma população de soluções evolui ao longo de gerações por meio de seleção (indivíduos com melhor fitness têm mais chance de reprodução), crossover (combina genes de dois pais) e mutação (introduz variação aleatória). Ao longo das gerações, a população converge para soluções ótimas ou próximas do ótimo — útil quando o espaço de busca é muito grande e não há uma forma analítica direta de encontrar o ótimo (ex.: caixeiro viajante, N-Rainhas, mochila 0-1, todos praticados em [`atividades/04-algoritmos-geneticos`](../atividades/04-algoritmos-geneticos/)).

**Explique o conceito de aprendizagem online e como ele difere da aprendizagem em batch.** *(resposta complementar)*
R: Na aprendizagem online, o modelo é atualizado incrementalmente à medida que novos dados chegam, sem precisar retreinar do zero — adequada a fluxos contínuos de dados e cenários que exigem adaptação em tempo real. Na aprendizagem em batch, o modelo é treinado de uma só vez com todo o conjunto de dados disponível; é mais simples, mas menos adaptável a mudanças que ocorrem depois do treinamento.

**Qual é a diferença entre busca em largura e busca em profundidade em termos de estratégia de exploração de nós?** *(resposta complementar)*
R: A busca em largura (BFS) explora todos os nós de uma camada (mesma distância da raiz) antes de avançar para a próxima camada — exploração "horizontal". A busca em profundidade (DFS) explora um ramo inteiro até o fim antes de retroceder e explorar outro ramo — exploração "vertical".

**Quais são as vantagens da busca em largura em relação à busca em profundidade?** *(resposta complementar)*
R: BFS garante encontrar o caminho mais curto (em número de passos) e é completa — sempre encontra uma solução se ela existir em um espaço de busca finito — sem risco de ficar presa em ramos infinitos, como pode acontecer com a DFS em grafos com ciclos.

**Quais são as vantagens da busca em profundidade em relação à busca em largura?** *(resposta complementar)*
R: DFS consome muito menos memória, pois só precisa armazenar o caminho atual da raiz até o nó corrente (mais os nós irmãos ainda não explorados), enquanto BFS precisa manter em memória todos os nós de uma camada inteira, que pode crescer exponencialmente.

**Em que tipo de problemas a busca em largura é mais adequada?** *(resposta complementar)*
R: Quando o objetivo é garantir o caminho mais curto e o espaço de busca é relativamente raso ou tem largura controlada (poucos nós por nível), de forma que o consumo de memória permaneça viável.

**Em que tipo de problemas a busca em profundidade é mais adequada?** *(resposta complementar)*
R: Quando a memória disponível é limitada, o espaço de busca é muito amplo (muitos nós por nível), ou quando se sabe que soluções aceitáveis tendem a estar em ramos profundos da árvore de busca.

**Como o algoritmo de busca em largura é implementado em termos de estrutura de dados e lógica de busca?** *(resposta complementar)*
R: Usa uma fila (estrutura FIFO — primeiro a entrar, primeiro a sair). O nó inicial é inserido na fila; a cada iteração remove-se o nó da frente da fila, verifica-se se é o objetivo e, caso não seja, inserem-se seus vizinhos ainda não visitados no final da fila. Ver pseudocódigo em [`material-aulas/pseudocodigos.md`](../material-aulas/pseudocodigos.md#busca-em-largura-bfs).

**Como o algoritmo de busca em profundidade é implementado em termos de estrutura de dados e lógica de busca?** *(resposta complementar)*
R: Usa uma pilha (estrutura LIFO — último a entrar, primeiro a sair), explícita ou implícita via recursão: o algoritmo expande sempre o nó mais recentemente adicionado, avançando o mais fundo possível, e retrocede (backtrack) quando um nó não tem mais vizinhos não visitados para explorar. Ver pseudocódigo em [`material-aulas/pseudocodigos.md`](../material-aulas/pseudocodigos.md#busca-em-profundidade-dfs).

**Como funciona o algoritmo A\* em comparação com a busca em largura e busca em profundidade?** *(resposta complementar)*
R: O A* usa uma função de avaliação f(n) = g(n) + h(n), combinando o custo real já percorrido até o nó (g) com uma estimativa heurística do custo restante até o objetivo (h), e expande sempre o nó de menor f(n). Diferente de BFS e DFS — que não usam nenhuma informação sobre a distância até o objetivo (busca não informada) —, o A* é uma busca informada, guiada pela heurística, e por isso geralmente explora muito menos nós para chegar à solução.

**Quais são as heurísticas comuns usadas no algoritmo A\*?** *(resposta complementar)*
R: Distância euclidiana (linha reta entre dois pontos), distância de Manhattan (soma das diferenças absolutas em cada eixo — comum em grades, como no 8-puzzle), e heurísticas específicas do domínio, como a distância em linha reta até o destino usada no problema do Mapa da Romênia (ver [`atividades/03-busca-informada-a-estrela`](../atividades/03-busca-informada-a-estrela/)).

**Quais são as vantagens do algoritmo A\* em relação à busca em largura e busca em profundidade?** *(resposta complementar)*
R: O A* é completo e ótimo (garante encontrar o caminho de menor custo) desde que a heurística seja admissível (nunca superestime o custo real restante), e costuma ser muito mais eficiente que BFS/DFS, pois evita explorar nós que claramente não levam a uma solução melhor que a já encontrada.
