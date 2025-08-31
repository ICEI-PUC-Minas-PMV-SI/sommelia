# Introdução

O SommelIA é um sistema inteligente de recomendação de vinhos que utiliza técnicas avançadas de aprendizado de máquina para analisar um extenso dataset de reviews de vinhos e fornecer sugestões personalizadas aos usuários. O projeto visa resolver o problema de escolha de vinhos, considerando as preferências individuais do usuário, características palatáveis dos vinhos, harmonização com alimentos e contexto de consumo. O sistema será desenvolvido para auxiliar tanto consumidores iniciantes quanto entusiastas de vinho, oferecendo uma experiência personalizada baseada em análise de dados, predições de qualidade e insights sobre regiões produtoras e variedades de uva.

O projeto se insere no contexto da transformação digital do setor vitivinícola, onde a tecnologia pode democratizar o acesso ao conhecimento especializado e melhorar significativamente a experiência de compra e consumo de vinhos. O SommelIA representa uma solução inovadora que combina análise de dados, processamento de linguagem natural e algoritmos de recomendação para criar um assistente virtual especializado em vinhos.

# Problema

A escolha de vinhos representa um desafio significativo para consumidores, especialmente considerando a vasta variedade disponível no mercado global. Muitas pessoas enfrentam dificuldades para encontrar vinhos que se alinhem com suas preferências de sabor, orçamento, ocasião de consumo e harmonização com alimentos. O problema se agrava pela falta de conhecimento técnico sobre características dos vinhos, regiões produtoras, técnicas de vinificação e padrões de qualidade.

O mercado de vinhos é altamente subjetivo e fragmentado, com avaliações que podem variar significativamente entre diferentes especialistas, críticos e consumidores. A terminologia técnica utilizada nas descrições de vinhos (como "taninos aveludados", "acidez vibrante", "corpo médio") cria barreiras de compreensão para o público leigo. Além disso, a relação qualidade-preço nem sempre é transparente, dificultando a tomada de decisão informada.

O contexto de aplicação será um sistema web responsivo e acessível, que permitirá aos usuários inserir informações detalhadas sobre suas preferências de sabor (doce, seco, frutado, herbáceo), orçamento disponível, tipo de uva preferida, região de origem desejada e ocasião de consumo (jantar romântico, celebração, harmonização com pratos específicos). O sistema utilizará o dataset WineMag com mais de 130 mil avaliações de vinhos realizadas por especialistas certificados para fornecer recomendações personalizadas, análises preditivas de qualidade e insights sobre harmonização.

# Questão de pesquisa

Como podemos utilizar técnicas avançadas de aprendizado de máquina e processamento de linguagem natural para criar um sistema de recomendação de vinhos que, baseado nas preferências pessoais do usuário, características palatáveis dos vinhos e contexto de consumo, seja capaz de predizer a qualidade esperada, sugerir opções relevantes e fornecer explicações interpretáveis sobre as recomendações, considerando fatores como variedade de uva, região produtora, preço, avaliações de especialistas e análise semântica das descrições textuais?

# Objetivos preliminares

**Objetivo geral:** Desenvolver e experimentar modelos de aprendizado de máquina e técnicas de processamento de linguagem natural para criar um sistema inteligente de recomendação, predição de qualidade e análise semântica de vinhos, considerando múltiplas dimensões de preferência do usuário.

**Objetivo específico 1:** Implementar um sistema de recomendação híbrido baseado em filtragem colaborativa, análise de conteúdo e processamento de linguagem natural, considerando características dos vinhos, preferências dos usuários e contexto de consumo para maximizar a relevância das sugestões.

**Objetivo específico 2:** Desenvolver modelos preditivos robustos para estimar a pontuação de qualidade de vinhos baseado em seus atributos estruturados (variedade, região, preço, vinícola) e não estruturados (descrições textuais), utilizando técnicas de ensemble learning e deep learning para capturar padrões complexos nos dados.

**Objetivo específico 3:** Criar um sistema de análise semântica que extraia características palatáveis e sensoriais das descrições textuais dos vinhos, permitindo a criação de perfis de sabor detalhados e melhorando a precisão das recomendações baseadas em preferências gustativas.

# Justificativa

O mercado de vinhos representa um setor econômico significativo e em crescimento, com o Brasil consumindo aproximadamente 400 milhões de litros anualmente, segundo dados da Organização Internacional da Vinha e do Vinho (OIV). O mercado global de vinhos movimenta mais de US$ 400 bilhões anualmente, demonstrando a relevância econômica do setor. A dificuldade na escolha de vinhos impacta diretamente a experiência do consumidor, pode limitar o crescimento do setor e representa uma oportunidade significativa para inovação tecnológica.

A escolha dos objetivos específicos se justifica pela necessidade de abordar de forma holística os múltiplos aspectos do problema de recomendação de vinhos. O sistema de recomendação híbrido atende à demanda por personalização e precisão, considerando tanto aspectos colaborativos quanto de conteúdo. Os modelos preditivos oferecem transparência sobre os fatores que influenciam a qualidade dos vinhos, permitindo aos usuários entender melhor o que esperar de cada produto. O sistema de análise semântica representa uma inovação significativa ao extrair insights de qualidade a partir de descrições textuais, superando as limitações dos atributos estruturados tradicionais.

A relevância do estudo se manifesta na aplicação prática de técnicas avançadas de machine learning para resolver um problema real e complexo do mercado consumidor, além de contribuir para a democratização do conhecimento sobre vinhos. O impacto social se reflete na melhoria da experiência de compra e consumo, facilitando o acesso a produtos de qualidade adequada ao perfil de cada usuário. O impacto econômico se manifesta no aumento da confiança do consumidor e na potencial expansão do mercado de vinhos premium e de qualidade.

# Público-Alvo

O sistema SommelIA se destina a diferentes perfis de usuários com necessidades variadas e níveis de expertise distintos:

**Consumidores iniciantes:** Pessoas com interesse em vinhos mas conhecimento limitado sobre variedades, regiões, harmonização e terminologia técnica. Buscam orientação clara e acessível para fazer escolhas adequadas ao seu paladar, orçamento e ocasião. Precisam de explicações simples sobre características dos vinhos e sugestões de harmonização com alimentos.

**Entusiastas de vinho:** Conhecedores com nível intermediário de expertise que desejam explorar novas opções, validar suas escolhas através de análises preditivas e aprofundar seu conhecimento sobre regiões produtoras e técnicas de vinificação. Buscam recomendações sofisticadas e insights detalhados sobre qualidade.

**Profissionais do setor:** Sommeliers, vendedores especializados, restaurantes e distribuidores que podem utilizar o sistema como ferramenta de apoio para recomendações, análise de produtos e treinamento de equipes. Necessitam de funcionalidades avançadas e dados detalhados sobre tendências de mercado.

**Lojas e distribuidores:** Empresas que buscam entender melhor as preferências dos consumidores, otimizar seu portfólio de produtos e desenvolver estratégias de marketing baseadas em dados. Precisam de análises agregadas e insights sobre comportamento de compra.

Todos os perfis compartilham a necessidade de um sistema intuitivo, com interface clara e responsiva, recomendações fundamentadas em dados reais de avaliações de especialistas, e funcionalidades que se adaptem ao nível de conhecimento do usuário. O sistema deve oferecer tanto recomendações simples para iniciantes quanto análises profundas para usuários avançados.

# Estado da arte 

## 1) Katumullage et al. (2022) — “Using Neural Network Models for Wine Review Classification”
- **Problema & contexto:** verificar se textos de reviews carregam informação suficiente para prever faixas de notas (Wine Spectator); comparação entre arquiteturas de NLP.  
- **Dados:** ~140k reviews (2006–2015) do Wine Spectator; notas 80–100; forte desbalanceamento entre classes. Pré-processamento básico (lowercase, remoção de pontuação; sem lematização agressiva por causa de modelos NN).  
- **Abordagem/algoritmos:** CNN, BiLSTM e BERT, com fine-tuning para classificação binária (≥90 vs. 80–89) e 4 classes (80–84, 85–89, 90–94, 95–100).  
- **Métricas:** **acurácia** entre modelos.  
- **Resultados:** BERT teve melhor desempenho—**89,12%** (binário) e **81,57%** (4 classes), superando SVMs de trabalhos anteriores. Limitações: uso de reviews de experts (não consumidores) e foco em acurácia.  
- **Referência:** Journal of Wine Economics, v17(1), 2022. DOI: 10.1017/jwe.2022.2.

## 2) Yang et al. (2022) — “Wine Review Descriptors as Quality Predictors”
- **Problema & contexto:** texto das reviews versus variáveis numéricas (preço, idade) na predição de “alta qualidade” (binário).  
- **Dados:** ~300k vinhos do Wine Spectator; representação de texto via **TF-IDF** e **Doc2Vec** combinada a numéricas (preço/idade).  
- **Abordagem:** **Regressão logística** com diferentes combinações de features.  
- **Métricas:** **acurácia** de classificação binária.  
- **Resultados:** descritores textuais superam variáveis numéricas para prever qualidade; ganhos modestos ao adicionar preço/idade. Limitação: modelo linear e avaliação restrita a acurácia.  
- **Referência:** Journal of Wine Economics, 2022 (open access).

## 3) Bender et al. (2023, NeurIPS) — “WineSensed: A Multimodal Wine Dataset”
- **Problema & contexto:** disponibilizar **grande dataset multimodal** (imagens de rótulos + reviews + metadados + anotações sensoriais humanas) para modelagem de sabor e preferência.  
- **Dados:** **824k reviews**, **897k imagens de rótulos**, >350k vinhos, metadados (ano, região, teor alcoólico, preço, uvas) a partir do **Vivino**; +5k pares de similaridade de sabor anotados por **256 participantes**.  
- **Abordagem:** propõe **FEAST**, um embedding conceitual que alinha kernels de máquina com distâncias sensoriais humanas.  
- **Métricas:** melhorias em tarefas de classificação “coarse” (país, uva, preço, rating) e alinhamento com proximidade sensorial (“TAR” no paper).  
- **Resultados:** embeddings multimodais melhoram predições de sabor/atributos; cria base sólida para recomendadores **multimodais** e **aprendizado de preferências**. Limitações: acesso/uso dos dados Vivino e viés de plataforma.  
- **Referência:** NeurIPS 2023 Datasets & Benchmarks; página do paper/dataset disponível.

## 4) Bjanes et al. (2024) — “A Recommender-Network Perspective of Review-Based Wine Recommendations”
- **Problema & contexto:** comparar **críticos vs. amadores** para avaliar dimensão social dos reviews e implicações em recomendação.  
- **Dados:** rede de avaliações; foco em estrutura/viés entre grupos (detalhes no preprint).  
- **Abordagem:** perspectiva de **rede de recomendação** com análise de pares/críticas.  
- **Métricas:** “**pairwise correctness**” em ranking e outras métricas de rede.  
- **Resultados:** diferenças sistemáticas entre críticos e usuários comuns impactam ranqueamento e recomendação; reforça necessidade de **personalização** e tratamento de **viés de origem do review**. Limitação: preprint e possível ausência de validação em produção.  
- **Referência:** arXiv:2404.07938, 2024.

## 5) Yano, Hakamata & Iwata (2024) — “WineGraph: Where is my Favourite Wine?”
- **Problema & contexto:** **recomendação e navegação** no espaço de vinhos com **grafo de similaridade** e embeddings de review.  
- **Dados:** reviews textuais e metadados; constrói grafo de vinhos/descritores.  
- **Abordagem:** **TF-IDF** + **Doc2Vec**/**GloVe** para embeddings; grafo de co-ocorrências; ranqueamento por similaridade e **PageRank**/**random walk** para descoberta.  
- **Métricas:** **Precision@k**, **Recall@k**, **nDCG@k** em tarefas de recuperação semelhante.  
- **Resultados:** grafos oferecem navegação interpretável para usuários (e pairing) e bom desempenho top-k; limitações de cobertura/viés do corpus.  
- **Referência:** Lecture Notes in Computer Science, Springer (2024).

## 6) Redelinghuys (2023) — “soMLier: A South African Wine Recommender System” (dissertação)
- **Problema & contexto:** construir um **recomendador de vinhos** focado em rótulos sul-africanos.  
- **Dados:** corpora de descrições/reviews e metadados locais.  
- **Abordagem:** **conteúdo-baseado** (TF-IDF/embeddings) + possíveis híbridos; protótipo web.  
- **Métricas:** **Precision@k**, **MAP**/**nDCG**.  
- **Resultados:** mostra viabilidade prática e desafios de **cold-start** e curadoria; enfatiza interpretabilidade para o usuário final.  
- **Referência:** Univ. of Cape Town, 2023.

## 7) Kim (2022) — “Predictions of Wine Ratings Using NLP”
- **Problema & contexto:** prever **nota numérica** (regressão) a partir de descrições textuais, comparando com preço/variedade/taster.  
- **Dados:** reviews com notas; inclui features de texto + preço/uva/país/taster.  
- **Abordagem:** **Decision Tree, Gradient Boosting, Random Forest**; vetorização de texto (bag-of-words/TF-IDF).  
- **Métricas:** **R²**.  
- **Resultados:** texto **supera preço** para prever qualidade; adicionar preço/variedade/taster melhora R² até **~0,59**. Limitações: modelos clássicos e ausência de métricas top-k de recomendação.  
- **Referência:** *Issues in Information Systems*, 2022. DOI: 10.48009/3_iis_2022_107.


# Síntese crítica

**Convergências.** Os estudos concordam que **texto de reviews porta forte sinal preditivo** sobre qualidade/preferência, frequentemente **superando variáveis numéricas simples** como preço ou idade. Modelos de **NLP modernos** (BERT) superam abordagens BoW/SVM e RNNs clássicas em classificação de faixas de nota. Para recomendação, **estruturas de similaridade** (grafos/embeddings) e **métricas de ranking** (Precision@k, nDCG@k) são adequadas e trazem interpretabilidade.

**Divergências.** Há variação quanto a **fontes de dados** (experts vs. usuários comuns), o que impacta o viés e o estilo do vocabulário. Papers diferem na **modalidade** (somente texto vs. multimodal com rótulos e metadados), e nas **métricas** (acurácia/R² vs. métricas top-k). Sistemas focados em um país (soMLier) priorizam cobertura e curadoria local, enquanto datasets globais (WineSensed) ampliam diversidade, porém com desafios de licenciamento e heterogeneidade.

**Lacunas.** Faltam benchmarks padronizados para **recomendação personalizada** de vinhos usando **preferências explícitas** do usuário. Pouco se mede **satisfação do usuário** e **explicabilidade** das sugestões (por notas sensoriais, pares com comida, budget). Há questões éticas/legais de **dados proprietários** (Vivino/Wine Spectator) e **viés de plataforma**. Também são raros estudos que tratem **cold-start** e avaliações **online** (A/B).

**Alinhamento ao seu projeto.** O seu Sommelier pode combinar:  
1) **NLP moderno** (BERT/Sentence-BERT) para embeddings sensoriais de reviews;  
2) **Recomendação multimodal** (texto + metadados + rótulos de imagens);  
3) **Grafos de similaridade** para navegação interpretável;  
4) **Preferências explícitas do usuário** mapeadas em embeddings;  
5) Avaliação com **métricas de ranking** (Precision@k, nDCG@k), **diversidade/novidade**, e **explicabilidade** (“recomendado por notas: ‘blackberry’, ‘oak’, tanino médio”).


Os estudos analisados demonstram consenso robusto sobre a eficácia de abordagens híbridas que combinam filtragem colaborativa com análise de conteúdo para sistemas de recomendação de vinhos. Há convergência clara sobre a importância de considerar múltiplos fatores, incluindo características palatáveis dos vinhos, preferências dos usuários, contexto de uso e evolução temporal das preferências. Os estudos concordam sobre o valor da análise de texto para extrair insights de qualidade que não são capturados pelos atributos estruturados tradicionais.

As principais divergências aparecem na escolha de algoritmos específicos, com alguns estudos favorecendo abordagens baseadas em deep learning enquanto outros demonstram superioridade de métodos ensemble tradicionais. Há também variação significativa na definição e implementação de métricas de avaliação, especialmente para aspectos como diversidade e novidade das recomendações.

As principais lacunas identificadas incluem a limitação de datasets com informações contextuais abrangentes e temporalmente consistentes, a necessidade de métricas de avaliação mais sofisticadas que considerem diversidade, novidade e interpretabilidade das recomendações, e a falta de estudos sobre personalização baseada em preferências evolutivas dos usuários em cenários reais de uso. Limitações técnicas incluem a necessidade de modelos mais interpretáveis e a escassez de estudos sobre escalabilidade em sistemas de produção.

O projeto SommelIA se alinha aos estudos identificados ao propor uma abordagem híbrida que considera tanto aspectos colaborativos quanto de conteúdo, além de incorporar análise preditiva de qualidade e processamento de linguagem natural. A utilização do dataset WineMag com 130 mil avaliações oferece uma base sólida para implementar as técnicas identificadas na literatura, enquanto a abordagem multimodal (estruturado + não estruturado) representa uma inovação que pode superar as limitações identificadas nos estudos existentes.

# Descrição do dataset selecionado

## Identificação e origem  
- **Nome:** Wine Reviews Dataset  
- **Fonte:** [Kaggle – Wine Reviews](https://www.kaggle.com/datasets/zynicide/wine-reviews)  
- **Instituição responsável:** Coletado da revista *Wine Enthusiast*, disponibilizado por contribuintes no Kaggle.  
- **Licença de uso:** Licença pública do Kaggle (destinada a uso educacional e de pesquisa).  

---

## Visão geral  
O dataset contém **129.971 registros**.  
- **Total de atributos:** 13  
- **Período coberto:** Diversas safras, com registros de vinhos de diferentes anos, regiões e países.  
- **Contextualização:** Cada linha representa um vinho avaliado por especialistas, incluindo informações sobre origem (país, região, vinícola), características (variedade de uva, denominação) e avaliações (descrição, pontuação, preço, nome do avaliador).  

---

## Atributos  

| Nome                   | Descrição                                                                 | Tipo      | Unidade      | Exemplo de valores |
|------------------------|---------------------------------------------------------------------------|-----------|--------------|---------------------|
| `country`              | País de origem do vinho.                                                  | Texto     | -            | US, Spain, Italy |
| `description`          | Texto descritivo do vinho elaborado pelo avaliador.                       | Texto     | -            | “Ripe aromas of fig, blackberry and cassis…” |
| `designation`          | Nome específico da linha ou denominação do vinho.                         | Texto     | -            | Reserve, Martha’s Vineyard |
| `points`               | Nota atribuída ao vinho pelo avaliador (escala 80–100).                   | Inteiro   | Pontos       | 88, 96 |
| `price`                | Preço do vinho em dólares.                                                | Numérico  | USD          | 15.0, 235.0 |
| `province`             | Província/estado de origem.                                               | Texto     | -            | California, Tuscany |
| `region_1`             | Região vinícola principal.                                                | Texto     | -            | Napa Valley, Rioja |
| `region_2`             | Sub-região vinícola (quando disponível).                                  | Texto     | -            | Central Coast |
| `taster_name`          | Nome do avaliador.                                                        | Texto     | -            | Roger Voss |
| `taster_twitter_handle`| Identificador do avaliador no Twitter.                                    | Texto     | -            | @vossroger |
| `title`                | Nome completo do vinho (vinícola, variedade, safra).                      | Texto     | -            | “Château les Ormes de Pez 2014 Saint-Estèphe” |
| `variety`              | Tipo de uva principal utilizada.                                          | Texto     | -            | Pinot Noir, Cabernet Sauvignon |
| `winery`               | Nome da vinícola produtora.                                               | Texto     | -            | Heitz, Maryhill |

---

## Qualidade dos dados  
- **Valores faltantes:**  
  - Presentes em vários atributos. Exemplo: `region_2` com 61.13% ausentes; `designation` com 28.82%; `price` com 6.9%.  
  - Alguns campos completos: `points`, `description`, `title`, `variety`, `winery`.  

- **Inconsistências:** 
  - Atributos de avaliadores (`taster_name`, `taster_twitter_handle`) podem não ser relevantes para modelos preditivos e possuem uma taxa de 20% a 24% de dados faltantes

- **Duplicatas:**  
  - O campo `title` é quase único (999 valores distintos em 1000 registros), indicando baixa incidência de duplicatas.

- **Outliers:**  
  - Possíveis outliers em `price`, com valores muito altos (ex.: acima de US$ 200, que representam vinhos raros).  
  - As notas (`points`) concentram-se entre 80 e 100, sem valores extremos fora do padrão.
  - Possui 10736 vinhos diferentes com mais de 2 avaliações.

# Canvas analítico

[O Canvas Analítico será preenchido integralmente conforme o modelo fornecido, considerando o modelo de negócio do SommelIA como sistema de recomendação inteligente de vinhos com potencial de monetização através de parcerias com vinícolas, lojas especializadas e plataformas de e-commerce.]

## Vídeo de apresentação da Etapa 01

[Será produzido vídeo de 5 a 8 minutos apresentando o trabalho realizado, com participação ativa de todos os integrantes do grupo, incluindo apresentação do problema, objetivos, justificativa, análise do estado da arte e descrição detalhada do dataset WineMag.]

# Referências

1. Katumullage, D.; Yang, C.; Barth, J.; Cao, J. *Using Neural Network Models for Wine Review Classification.* Journal of Wine Economics 17(1), 2022. DOI: 10.1017/jwe.2022.2.  
2. Yang, C.; Barth, J.; Katumullage, D.; Cao, J. *Wine Review Descriptors as Quality Predictors.* Journal of Wine Economics, 2022.  
3. Bender, T. et al. *Learning to Taste: A Multimodal Wine Dataset (WineSensed).* NeurIPS 2023.  
4. Bjanes, S. S. et al. *A Recommender-Network Perspective of Review-Based Wine Recommendations.* arXiv:2404.07938, 2024.  
5. Yano, H.; Hakamata, M.; Iwata, D. *WineGraph: Where is my Favourite Wine?* In: Information Modelling and Knowledge Bases XXXIV, Springer, 2024.  
6. Redelinghuys, M. *soMLier: A South African Wine Recommender System.* MSc Thesis, Univ. of Cape Town, 2023.  
7. Kim, B. *Predictions of Wine Ratings Using NLP.* Issues in Information Systems 23(3), 2022. DOI: 10.48009/3_iis_2022_107.  