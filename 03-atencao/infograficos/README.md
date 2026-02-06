# Infográficos — Capítulo 03: Atenção (Self-Attention)

Este diretório contém os infográficos utilizados no Capítulo 03 da série
**Fazendo um LLM do Zero**.

Este capítulo foca no mecanismo mais revolucionário dos Transformers:
a capacidade de processar contexto e relacionar palavras distantes.

Os infográficos aqui têm como objetivo:
- visualizar como o contexto é construído
- desmistificar as matrizes Query, Key e Value
- explicar o funcionamento da máscara causal
- mostrar onde a atenção se encaixa na arquitetura maior

---

## 📊 Lista de Infográficos do Capítulo

### 01 — Contexto importa
**Arquivo:** `01-contexto-importa.svg`  
**Seção do diário:** *O problema do contexto*  

Ilustra por que a tradução palavra por palavra falha e como o significado
depende inteiramente do contexto da frase.

---

### 02 — Intuição da atenção
**Arquivo:** `02-self-attention-intuicao.svg`  
**Seção do diário:** *A ideia intuitiva da atenção*  

Mostra visualmente como cada palavra "olha" para outras palavras da frase
para decidir sua importância (pesos de atenção).

---

### 03 — Weighted context vector
**Arquivo:** `03-weighted-context.svg`  
**Seção do diário:** *Construindo vetores de contexto*  

Explica matematicamente como o vetor de contexto é calculado como uma
soma ponderada dos vetores de entrada.

---

### 04 — Projeções Q, K e V
**Arquivo:** `04-qkv-projecoes.svg`  
**Seção do diário:** *Introduzindo Query, Key e Value*  

Apresenta a analogia de banco de dados (Query, Key, Value) aplicada
ao processamento de linguagem natural.

---

### 05 — Self-attention treinável
**Arquivo:** `05-self-attention-treinavel.svg`  
**Seção do diário:** *Self-Attention com pesos treináveis*  

Mostra como as matrizes de peso ($W_q, W_k, W_v$) transformam embeddings
em projeções que o modelo pode aprender.

---

### 06 — Máscara causal
**Arquivo:** `06-causal-mask.svg`  
**Seção do diário:** *Máscara causal: impedindo o modelo de ver o futuro*  

Visualiza a matriz triangular que bloqueia o acesso a tokens futuros,
essencial para o treinamento autoregressivo (GPT).

---

### 07 — Dropout na atenção
**Arquivo:** `07-dropout-attention.svg`  
**Seção do diário:** *Dropout na atenção*  

Ilustra como o dropout zera aleatoriamente alguns pesos de atenção
durante o treino para prevenir overfitting.

---

### 08 — Multi-head attention
**Arquivo:** `08-multi-head.svg`  
**Seção do diário:** *Multi-Head Attention*  

Mostra como dividir o processamento em múltiplas "cabeças" permite
que o modelo capture diferentes tipos de relações simultaneamente.

---

### 09 — Self-attention no Transformer
**Arquivo:** `09-self-attention-no-transformer.svg`  
**Seção do diário:** *Onde a atenção entra no Transformer*  

Situa o bloco de atenção dentro da arquitetura completa, mostrando
sua conexão com as camadas de entrada e saída.

---

## 🎨 Diretrizes visuais

Todos os infográficos devem:
- manter consistência visual entre si
- usar cores suaves e profissionais
- evitar excesso de texto
- priorizar leitura rápida em artigos técnicos (Medium / Dev.to)