# Etapa 3 — Modelagem, Avaliação e Pipeline

## Preparação dos dados

Nesta etapa, foram aplicadas diversas técnicas de **pré-processamento e tratamento dos dados textuais** com o objetivo de preparar as descrições dos vinhos para a aplicação de modelos de aprendizado de máquina voltados à análise semântica.

### 1. Limpeza de dados
- **Remoção de valores ausentes:** as descrições (`description`) nulas foram eliminadas, uma vez que o modelo semântico depende diretamente do texto para gerar embeddings.  
- **Remoção de duplicatas:** registros com textos idênticos foram removidos para evitar distorções nas análises.  
- **Normalização textual:** todas as descrições foram convertidas para letras minúsculas e tiveram pontuações, caracteres especiais e espaços duplicados removidos.  
- **Tratamento de outliers:** não foi necessária a remoção de outliers numéricos, pois o foco da análise é textual e não quantitativo.

### 2. Transformação dos dados
- **Tokenização e limpeza linguística:** foram removidas *stopwords* (palavras de pouco significado semântico, como “de”, “em”, “com”) e termos genéricos relacionados a vinho (“wine”, “grape”, “flavor”, etc.), visando realçar os elementos descritivos mais relevantes.  
- **Codificação textual:** os textos foram preparados para serem transformados em vetores numéricos densos por meio de embeddings semânticos.  
- **Padronização dos dados:** os textos foram processados de forma homogênea para que o modelo tratasse todas as entradas dentro da mesma estrutura linguística.

### 3. Feature Engineering
- Criação de uma nova variável baseada no **vetor semântico** de cada descrição, gerado por meio do modelo `SentenceTransformer('all-MiniLM-L6-v2')`.  
- Esses vetores, com 384 dimensões, representam as relações de significado entre as sentenças e formam a base para a análise de similaridade e agrupamento textual.

### 4. Separação dos dados
Como a análise teve natureza **não supervisionada**, não houve divisão tradicional em conjuntos de treinamento e teste.  
Os embeddings foram gerados para todo o corpus, e a avaliação foi feita de forma interpretativa, observando os agrupamentos e as distâncias semânticas entre os textos.

### 5. Redução de dimensionalidade (opcional)
Para facilitar a visualização, técnicas como **PCA** ou **UMAP** podem ser aplicadas para reduzir as 384 dimensões dos embeddings a 2 ou 3, permitindo observar graficamente as relações semânticas entre as descrições.

---

## Descrição do modelo

O modelo selecionado para esta etapa foi o **`all-MiniLM-L6-v2`**, parte da família **Sentence-BERT (SBERT)**, disponibilizado pela biblioteca **SentenceTransformer**.  

### Conceitos e princípios de funcionamento
O modelo `all-MiniLM-L6-v2` é uma versão leve e eficiente do SBERT, que transforma sentenças em **vetores de embeddings semânticos**.  
Esses vetores permitem calcular **similaridades entre textos** baseadas em significado, e não apenas em palavras exatas.  

Enquanto modelos tradicionais de *bag-of-words* consideram apenas a frequência de palavras, o SBERT utiliza redes neurais transformadoras (*Transformers*) para capturar o **contexto e o sentido** das frases, gerando representações numéricas ricas e interpretáveis.

### Vantagens
- Elevada **eficiência computacional**, mesmo em grandes volumes de dados.  
- Capacidade de **entender contexto e sinonímias**, superando abordagens baseadas apenas em contagem de palavras.  
- Geração de embeddings reutilizáveis para diferentes tarefas (busca, clustering, classificação).

### Limitações
- Pode apresentar **perda de nuances culturais ou linguísticas** em textos regionais.  
- Embora multilíngue, o modelo é otimizado principalmente para o inglês, o que pode reduzir levemente a precisão em textos totalmente em português.  

### Justificativa da escolha
A escolha do modelo `all-MiniLM-L6-v2` se deu por seu equilíbrio entre **velocidade, desempenho semântico e leveza**, sendo ideal para aplicações exploratórias e prototipagem.  
Outros modelos maiores, como `paraphrase-multilingual-MiniLM-L12-v2`, podem ser considerados em etapas futuras para refinar a análise em contextos multilíngues.

---

## Avaliação do modelo criado

### Métricas utilizadas

Por se tratar de uma análise **não supervisionada**, não foram utilizadas métricas tradicionais como acurácia, precisão ou F1-Score.  
Em vez disso, a avaliação baseou-se em **métricas qualitativas**, observando:

- **Coerência dos agrupamentos:** verificação se descrições semanticamente semelhantes (ex: “aroma frutado e fresco”) se aproximavam no espaço vetorial.  
- **Separação temática:** análise da distância entre grupos de descrições distintas (ex: vinhos doces vs. vinhos encorpados).  
- **Eficiência computacional:** tempo de processamento e  consumo de memória durante a geração dos embeddings.

### Discussão dos resultados obtidos

O modelo demonstrou bom desempenho na **organização semântica** das descrições.  
As observações mostraram que textos com padrões semelhantes foram agrupados de maneira coerente, validando a capacidade do modelo em identificar significados próximos mesmo em diferentes estruturas gramaticais.  

Além disso, a visualização dos embeddings reduziu a complexidade dos dados e revelou **tendências e relações linguísticas** interessantes, como a correlação entre termos positivos e notas mais altas de vinho.  

Os resultados reforçam que o uso de embeddings semânticos é uma ferramenta poderosa para a compreensão de textos descritivos e pode ser expandida para tarefas como **classificação de sentimento**, **recomendação** e **análise de tópicos**.

---

## Pipeline de pesquisa e análise de dados

O pipeline desenvolvido para esta pesquisa foi estruturado em etapas sequenciais e replicáveis, garantindo clareza e reprodutibilidade dos resultados.  

**Etapas do pipeline:**

1. **Coleta dos dados**  
   - Base textual contendo descrições de vinhos e seus metadados (nota, preço, país, tipo de uva etc.).  

2. **Limpeza e pré-processamento**  
   - Remoção de valores nulos, duplicatas e ruídos textuais.  
   - Padronização e normalização dos textos.

3. **Geração dos embeddings**  
   - Aplicação do modelo `all-MiniLM-L6-v2` para converter cada descrição em um vetor de 384 dimensões.

4. **Análise exploratória e semântica**  
   - Cálculo de similaridades entre textos.  
   - Identificação de agrupamentos e padrões de linguagem.  
   - Visualização da distribuição dos embeddings em 2D.

5. **Interpretação e conclusões**  
   - Avaliação qualitativa dos agrupamentos e padrões encontrados.  
   - Registro dos resultados e insights extraídos do modelo.

Esse pipeline permite **reutilização e adaptação** para outros conjuntos de dados textuais, bastando substituir o corpus e manter o mesmo fluxo de pré-processamento e análise.

---

## Observações importantes

Todas as tarefas realizadas nesta etapa foram registradas em formato de texto, acompanhadas das explicações e resultados interpretativos.  
Os códigos utilizados encontram-se na pasta **`src`** deste projeto, seguindo a estrutura definida para esta etapa da pesquisa.
