
# Capítulo 07 — Instruction Tuning

Nos capítulos anteriores, construímos progressivamente um modelo de linguagem completo:

- Capítulo 01 — O que é um LLM  
- Capítulo 02 — Como texto vira números  
- Capítulo 03 — Como o modelo constrói contexto com atenção  
- Capítulo 04 — Construindo um GPT do zero  
- Capítulo 05 — Como modelos aprendem linguagem  
- Capítulo 06 — Fine-Tuning para Classificação  

Neste capítulo final exploramos um dos avanços mais importantes da evolução dos LLMs:

> Ensinar modelos a seguir instruções humanas.

---

## 🎯 Objetivo do Capítulo

Ao final deste capítulo, você deverá ser capaz de:

- entender o conceito de instruction tuning
- compreender como modelos conversacionais são treinados
- preparar datasets de instruções e respostas
- aplicar supervised fine-tuning para geração orientada
- entender mascaramento de loss em tarefas conversacionais
- avaliar respostas geradas por modelos
- compreender como surgem assistentes baseados em LLMs

Este capítulo representa a transição entre **modelos que aprendem linguagem** e **modelos que interagem com pessoas**.

---

## 🧭 Como este capítulo está organizado

O conteúdo segue uma progressão conceitual até a implementação prática.

---

### 1. O que é Instruction Tuning

Nesta seção exploramos como modelos passam de prever texto para responder instruções.

Serão discutidos:

- modelos base vs modelos alinhados
- supervised fine-tuning
- papel do comportamento conversacional
- evolução histórica dos LLMs

---

### 2. Estrutura de Dados para Instruções

Aqui estudamos como preparar datasets que ensinam o modelo a responder perguntas e executar tarefas.

Serão abordados:

- estrutura instruction / input / response
- formatação de prompts estruturados
- padronização de dados conversacionais
- impacto da qualidade do dataset

---

### 3. Mascaramento da Loss

Instruction tuning utiliza uma estratégia importante:

O modelo aprende apenas com a parte da resposta.

Nesta seção exploramos:

- como separar prompt e resposta
- por que mascarar tokens do prompt
- como isso influencia o comportamento do modelo
- impacto no aprendizado supervisionado

---

### 4. Pipeline de Supervised Fine-Tuning (SFT)

Nesta seção implementamos o pipeline completo de instruction tuning:

- preparação do dataset de instruções
- tokenização estruturada
- treinamento supervisionado para geração
- reutilização de pesos pré-treinados
- monitoramento do treinamento

---

### 5. Avaliação de Modelos Instruction-Tuned

Modelos conversacionais não são avaliados apenas por métricas numéricas.

Serão exploradas formas de avaliação:

- comparação qualitativa de respostas
- análise de coerência e relevância
- validação manual de outputs
- limitações das métricas tradicionais

---

### 6. Uso Prático e Aplicações

Depois do treinamento, exploramos como utilizar o modelo para:

- responder perguntas abertas
- executar tarefas simples
- interagir com prompts estruturados
- simular comportamento conversacional

---

## 🧪 Parte prática (notebook)

Este capítulo inclui um notebook executável no Google Colab que implementa:

- criação de dataset de instruções
- formatação de prompts estruturados
- adaptação do GPTMini para geração supervisionada
- treinamento supervisionado para respostas orientadas
- avaliação qualitativa de respostas
- comparação entre modelo base e modelo instruction-tuned

O notebook mantém foco didático e explicações passo a passo.

---

## 📊 Infográficos

Este capítulo utiliza infográficos para explicar:

- evolução de modelos base para modelos alinhados
- estrutura de datasets de instruções
- mascaramento de loss
- pipeline de supervised fine-tuning
- avaliação de respostas conversacionais

Os detalhes dos infográficos estão documentados em:
- `infograficos/README.md`

---

## ▶️ Como executar

1. Leia o diário do capítulo:
- `diario.md`

2. Execute o notebook:
- `notebook.ipynb`

3. Ou abra diretamente no Google Colab:
- veja `links.md`

---

## 🎥 Material complementar

Este capítulo é inspirado nas explicações e implementações do próprio autor do livro, que demonstra como modelos GPT podem ser adaptados para seguir instruções humanas.

O material complementar apresenta:

- construção de datasets conversacionais
- treinamento supervisionado orientado a respostas
- avaliação de comportamento de modelos

---

## 📘 Referência

Este capítulo é inspirado no Capítulo 7 do livro:

**Build a Large Language Model (From Scratch)**  
Sebastian Raschka

O conteúdo foi adaptado para:

- abordagem didática em português
- execução prática no Google Colab
- foco em compreensão conceitual do instruction tuning
- ampliação pedagógica dos conceitos apresentados no livro

---

## ⚠️ Observação importante

Instruction tuning é uma etapa fundamental na construção de assistentes baseados em LLMs.

Neste projeto utilizamos:

- datasets pequenos e educacionais
- modelos compactos
- treinamento simplificado

Essas simplificações permitem execução em ambientes educacionais, mantendo os princípios utilizados em sistemas reais.

---

## 🧠 Por que este capítulo é o encerramento da série

Neste ponto o leitor compreende:

- como modelos aprendem linguagem
- como modelos são adaptados para tarefas específicas
- como modelos aprendem a seguir instruções humanas
- como surgem assistentes baseados em LLMs
- como pipelines modernos de treinamento são estruturados

Este capítulo conecta todos os conceitos fundamentais necessários para compreender o funcionamento dos grandes modelos de linguagem modernos.
