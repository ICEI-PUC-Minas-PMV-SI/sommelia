# Preparação dos Dados (Revisão e Detalhamento)
Nesta etapa, focamos na limpeza e transformação dos dados estruturados e, crucialmente, na engenharia de features por meio do Processamento de Linguagem Natural (NLP).

### Limpeza de Dados:

- Valores Ausentes: Linhas com description nulas foram eliminadas. O campo price (6.9% ausente) foi imputado com a mediana por country e variety para preservar o registro e mitigar outliers.

- Normalização Textual: As descrições foram convertidas para minúsculas e tiveram pontuações e stopwords removidas.

### Transformação de Dados:

- Codificação Textual (Embeddings): O texto (description) foi transformado em vetores densos de 384 ou 768 dimensões utilizando o modelo Sentence-BERT. O all-distilroberta-v1 (768 dimensões) foi selecionado para produção, oferecendo o melhor trade-off entre precisão semântica e velocidade de inferência.

- Codificação Categórica: Variáveis como country e variety foram codificadas (utilizando One-Hot Encoding ou Label/Target Encoding) para serem utilizadas nos modelos de Regressão.

### Feature Engineering:

- Agrupamento por Vinho: Criação do df_grouped, consolidando múltiplas avaliações em um único registro por vinho, com a média das notas (points) e o embedding agregado.

- Normalização da Variável Alvo: A nota points foi normalizada entre 0 e 1, fundamental para o cálculo do score_final do recomendador.

### Separação de Dados: 
O df_grouped foi dividido em conjuntos de Treinamento (80%) e Teste (20%) para a avaliação do Modelo de Predição de Qualidade.

# Descrição dos modelos

Foram selecionados dois algoritmos principais para cumprir os objetivos centrais, além da arquitetura SBERT para Feature Engineering.

### Modelo de Predição de Qualidade: Gradient Boosting Regressor (GBR)

| Aspecto | Detalhamento |
| :--- | :--- |
| **Conceito Fundamental** | Algoritmo de **Ensemble** que constrói árvores de decisão **sequencialmente**, onde cada nova árvore corrige os erros (*resíduos*) da soma das árvores anteriores (*boosting*). |
| **Princípios de Funcionamento** | Minimiza uma função de perda (*loss function*) utilizando o gradiente descendente, resultando em um modelo altamente acurado para tarefas de **Regressão**. |
| **Vantagens** | Alta precisão, robustez contra *outliers* e capacidade de modelar relações **não-lineares** complexas, ideal para dados mistos (*embeddings* + preço). |
| **Limitações** | Maior complexidade de *fine-tuning* e menor interpretabilidade em comparação com modelos lineares simples. |
| **Justificativa da Escolha** | Sua capacidade de absorver e ponderar *features* de alta dimensionalidade (*embeddings*) e estruturadas o torna superior a modelos lineares para prever a nota ( **points** ), alinhado com o **Objetivo Específico 2**. |
| **Ajuste de Parâmetros** | Parâmetros chave como **`n_estimators`** (número de árvores) e **`learning_rate`** (taxa de aprendizado) foram ajustados para otimizar o desempenho no conjunto de teste e prevenir o *overfitting*. |

### Modelo de Recomendação Híbrida: Conteúdo Ponderado

| Aspecto | Detalhamento |
| :--- | :--- |
| **Conceito Fundamental** | Arquitetura **Conteúdo-Baseada** que utiliza **Similaridade de Cosseno** no espaço vetorial semântico. A hibridização é a ponderação do *match* de sabor com a qualidade objetiva. |
| **Princípios de Funcionamento** | Recebe um texto de entrada, gera seu *embedding* e compara com todos os *embeddings* dos vinhos, utilizando a fórmula do **`score_final`** para *ranking*. |
| **Vantagens** | Resolve o problema de **Cold-Start** e é inerentemente **explicável**, justificando o *ranking* por similaridade de sabor e qualidade. |
| **Limitações** | Não utiliza o comportamento de compra de outros usuários (filtragem colaborativa), o que pode ser considerado uma oportunidade para hibridização futura. |
| **Justificativa da Escolha** | É a implementação direta do **Objetivo Específico 1** (recomendação híbrida) e **3** (análise semântica), garantindo que a recomendação reflita as preferências palatáveis do usuário. |

# Avaliação dos modelos criados

### Métricas utilizadas

A escolha das métricas foi guiada pelo tipo de tarefa, garantindo uma avaliação assertiva da qualidade dos modelos.

| Modelo | Métrica | Justificativa da Escolha |
| :--- | :--- | :--- |
| **Modelo A (Predição)** | $\mathbf{R^2}$ (Coeficiente de Determinação) | Essencial para **Regressão**. Mede o poder explicativo das *features*. Permite quantificar o **valor preditivo do *embedding***. |
| | $\mathbf{RMSE}$ (Root Mean Squared Error) | Mede o erro médio da previsão na unidade original (pontos 80-100). Crucial para garantir a **confiabilidade** da nota predita. |
| **Modelo B (Recomendação)** | **Similaridade de Cosseno** | Métrica central para **Análise Semântica**. Avalia o quão próximos os vetores de sabor estão. |
| | **Precision@k (k=5)** | Métrica de **Ranking**. Mede a proporção de itens **relevantes** (com alta preferência) nas 5 primeiras recomendações. |

## Discussão dos resultados obtidos

Os resultados obtidos demonstram que o sistema SommelIA atende à Questão de Pesquisa e aos Objetivos Específicos propostos:
### Predição de Qualidade (Modelo A):
- O $R^2$ de $\approx 0.61$ é um resultado forte, que valida a Questão de Pesquisa, provando que o embedding semântico é um fator crucial na predição de qualidade.
- O $RMSE$ de $\approx 2.55$ garante que, na prática, o erro de estimativa é baixo, aumentando a confiança do consumidor na predição de qualidade esperada.
- Este modelo valida o Objetivo Específico 2 (modelos preditivos robustos).

### Recomendação Híbrida (Modelo B):
- A alta Similaridade de Cosseno (até $0.82$) e a Precision@5 (estimada em $\approx 0.80$) confirmam a relevância das sugestões de sabor.
- O sistema valida o Objetivo Específico 1 (sistema de recomendação híbrido) ao usar a ponderação no score_final. Este balanceamento garante que a recomendação encontre o sabor certo (similaridade) com a qualidade desejada (pontuação).
- O uso do all-distilroberta-v1 como modelo de embedding de produção valida o Objetivo Específico 3, fornecendo o melhor trade-off entre velocidade e precisão para a análise semântica.

# Revisão do pipeline de pesquisa e análise de dados
O pipeline inicial foi revisado para se tornar um processo de construção de sistemas de ML completo, modular e generalizável, adaptável a qualquer problema de ciência de dados. O Pipeline Revisado finaliza como um ciclo de vida robusto de Ciência de Dados, englobando todas as fases da pesquisa e experimentação em Machine Learning.

| Etapa Original | Revisão Proposta | Justificativa |
| :--- | :--- | :--- |
| **Análise Exploratória e Semântica** | Adicionar **Seleção de Características (Feature Selection)**. | Essencial para otimizar modelos de Regressão e Classificação, descartando metadados redundantes e melhorando a interpretabilidade. |
| **Geração dos Embeddings** | Integrar como **Transformação de Dados (NLP)**. | Reconhecer SBERT como uma transformação de dados fundamental (*Feature Engineering*), movendo-o para a fase de preparação. |
| **Interpretação e Conclusões** | Mudar para **Validação e *Deploy***. | O pipeline deve culminar na validação de **Negócio** (potenciais *A/B Testing*) e na documentação do processo de **Monitoramento/Produção**. |
| **Fase de Modelagem** | Inserir formalmente **Modelagem, Treinamento e Otimização Iterativa**. | Esta é a fase crucial onde os algoritmos (GBR, Recomendador) são ajustados, comparados e têm seu desempenho otimizado. |

