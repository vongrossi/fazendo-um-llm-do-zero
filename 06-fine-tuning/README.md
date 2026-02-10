# Capítulo 06 — Fine-Tuning para Classificação

Nos capítulos anteriores, construímos e treinamos um modelo GPT didático:

- Capítulo 01 — O que é um LLM  
- Capítulo 02 — Como texto vira números  
- Capítulo 03 — Como o modelo constrói contexto com atenção  
- Capítulo 04 — Construindo um GPT do zero  
- Capítulo 05 — Como modelos aprendem linguagem  

Agora chegamos a uma das aplicações mais importantes dos LLMs:

> Adaptar modelos pré-treinados para resolver tarefas específicas.

Neste capítulo exploramos como transformar um modelo GPT em um classificador supervisionado.

---

## 🎯 Objetivo do Capítulo

Ao final deste capítulo, você deverá ser capaz de:

- entender o conceito de fine-tuning
- compreender a diferença entre pré-treinamento e adaptação supervisionada
- transformar um modelo generativo em um modelo de classificação
- implementar uma camada de classificação sobre um GPT
- treinar o modelo com dados rotulados
- compreender estratégias de congelamento e ajuste de pesos
- avaliar desempenho com métricas de classificação
- usar o modelo treinado para prever classes de novos textos

Este capítulo marca a transição entre **modelos de linguagem gerais** e **modelos especializados em tarefas reais**.

---

## 🧭 Como este capítulo está organizado

O conteúdo segue uma progressão do entendimento conceitual até a implementação prática.

---

### 1. Pré-Treinamento vs Fine-Tuning

Nesta seção exploramos a diferença entre:

- modelos pré-treinados
- adaptação supervisionada para tarefas específicas

Serão discutidos:

- foundation models
- transferência de conhecimento
- especialização de modelos

---

### 2. Transformando GPT em um Classificador

Aqui estudamos como reutilizar o conhecimento linguístico do modelo para classificação.

Serão abordados:

- extração de representações contextuais
- pooling de embeddings
- adição de uma camada de classificação (classification head)
- adaptação do objetivo de treinamento

---

### 3. Estratégias de Fine-Tuning

Nesta seção exploramos diferentes abordagens para adaptar modelos:

- fine-tuning completo
- congelamento de camadas
- ajuste parcial do modelo
- impacto do tamanho do dataset
- trade-offs entre custo computacional e generalização

---

### 4. Treinamento Supervisionado

Implementamos o pipeline completo de treinamento para classificação:

- preparação de dataset rotulado
- tokenização de dados supervisionados
- treinamento com cross entropy para classes
- validação do modelo
- monitoramento de métricas

---

### 5. Avaliação de Modelos de Classificação

Serão exploradas métricas fundamentais:

- accuracy
- precision
- recall
- F1-score
- confusion matrix

Esta seção demonstra como avaliar modelos além da simples taxa de acerto.

---

### 6. Inferência e Uso Prático

Depois do treinamento, exploramos como utilizar o modelo para:

- classificar novos textos
- interpretar previsões
- analisar erros do modelo
- validar comportamento em cenários reais

---

## 🧪 Parte prática (notebook)

Este capítulo inclui um notebook executável no Google Colab que implementa:

- criação de um modelo GPT adaptado para classificação
- reutilização de pesos pré-treinados
- treinamento supervisionado com dataset rotulado
- comparação entre estratégias de fine-tuning
- avaliação com métricas de classificação
- inferência com novos textos

O notebook prioriza clareza conceitual e explicações passo a passo.

---

## 📊 Infográficos

Este capítulo utiliza infográficos para explicar:

- relação entre pré-treinamento e fine-tuning
- estrutura de um classification head
- estratégias de congelamento de camadas
- pipeline de treinamento supervisionado
- interpretação de métricas de classificação

Os detalhes dos infográficos estão documentados em:

- [infograficos/README.md](infograficos/README.md)

---

## ▶️ Como executar

1. Leia o diário do capítulo:
   - [diario.md](diario.md)

2. Execute o notebook:
   - [notebook.ipynb](notebook.ipynb)

3. Ou abra diretamente no Google Colab:
   - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vongrossi/fazendo-um-llm-do-zero/blob/main/06-fine-tuning/notebook.ipynb)
   - ou veja mais detalhes em [links.md](links.md)


---

## 🎥 Material complementar

Este capítulo é inspirado nas explicações e implementações do próprio autor do livro, que demonstra como modelos GPT podem ser adaptados para tarefas supervisionadas, como classificação de texto.

O material complementar apresenta:

- adaptação de modelos generativos
- exemplos práticos de classificação com LLMs
- demonstração de fine-tuning supervisionado

---

## 📘 Referência

Este capítulo é inspirado no Capítulo 6 do livro:

**Build a Large Language Model (From Scratch)**  
Sebastian Raschka

O conteúdo foi adaptado para:

- abordagem didática em português
- execução prática no Google Colab
- foco em compreensão conceitual do fine-tuning
- ampliação pedagógica dos conceitos apresentados no livro

---

## ⚠️ Observação importante

Fine-tuning é uma das técnicas mais utilizadas para adaptar LLMs para aplicações reais.

Neste projeto utilizamos:

- datasets pequenos
- modelos compactos
- treinamento simplificado

Essas simplificações permitem execução em ambientes educacionais, mantendo os princípios utilizados em sistemas de produção.

---

## 🧠 Por que este capítulo é fundamental

Neste é o momento onde fica compreensivel:

- como adaptar modelos para tarefas específicas
- como reutilizar conhecimento pré-treinado
- como preparar modelos para aplicações reais
- como avaliar qualidade em tarefas supervisionadas
- como evoluir para técnicas avançadas como instruction tuning e alinhamento de modelos

Após este capítulo, estaremos preparado para explorar aplicações práticas e especialização de LLMs.



