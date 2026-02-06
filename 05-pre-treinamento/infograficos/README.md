# Infográficos — Capítulo 05: Pré-Treinamento e Geração

Este diretório contém os infográficos utilizados no Capítulo 05 da série
**Fazendo um LLM do Zero**.

Neste capítulo exploramos como modelos GPT aprendem linguagem e como geram
texto após o treinamento.

Os infográficos deste capítulo ajudam a visualizar:
- o pipeline completo de treinamento
- como a função de perda mede erros
- o ciclo iterativo de aprendizado (loop)
- estratégias de geração de texto (decoding)
- persistência de modelos (checkpoints)

---

## 📊 Lista de Infográficos do Capítulo

### 01 — Pipeline de treinamento
**Arquivo:** `01-pipeline-treinamento.svg`  
**Seção do diário:** *O pipeline de treinamento de um LLM*  

Mostra o fluxo completo: Dataset → Tokenização → Forward Pass → Loss →
Backpropagation → Atualização de Pesos.

---

### 02 — Cross Entropy
**Arquivo:** `02-cross-entropy.svg`  
**Seção do diário:** *Cross Entropy: medindo o erro probabilístico*  

Ilustra como a função de perda compara a distribuição prevista pelo modelo
com o token real para calcular o erro.

---

### 03 — Loop de treinamento
**Arquivo:** `03-loop-treinamento.svg`  
**Seção do diário:** *O loop de treinamento completo*  

Visualiza o ciclo iterativo de batches e epochs que permite ao modelo
aprender gradualmente com os dados.

---

### 04 — Estratégias de decoding
**Arquivo:** `04-decoding-strategies.svg`  
**Seção do diário:** *Estratégias de geração de texto*  

Compara métodos de geração como Greedy, Temperature, Top-k e Nucleus Sampling,
mostrando como afetam criatividade e coerência.

---

### 05 — Checkpoints
**Arquivo:** `05-checkpoints.svg`  
**Seção do diário:** *Salvando modelos: checkpoints*  

Explica a importância de salvar estados intermediários do modelo para
retomada de treino e reutilização posterior.

---

## 🎨 Diretrizes visuais

Todos os infográficos devem:
- manter consistência visual entre si
- usar cores suaves e profissionais
- evitar excesso de texto
- priorizar leitura rápida em artigos técnicos (Medium / Dev.to)