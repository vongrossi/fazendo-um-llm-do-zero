# Infográficos — Capítulo 04: Construindo um GPT do Zero

Este diretório contém os infográficos utilizados no Capítulo 04 da série
**Fazendo um LLM do Zero**.

Este capítulo marca a transição entre compreender os componentes individuais
dos Transformers e construir um modelo GPT completo.

Os infográficos deste capítulo ajudam a visualizar:
- a estrutura interna de um bloco Transformer
- o fluxo de dados através das camadas
- o papel das redes feedforward e normalização
- a arquitetura completa do GPTMini

---

## 📊 Lista de Infográficos do Capítulo

### 01 — Estrutura de um Bloco Transformer
**Arquivo:** `01-transformer-block.svg`  
**Seção do diário:** *O bloco fundamental do Transformer*  

Mostra visualmente os quatro componentes principais de um bloco Transformer:
Self-Attention, Feedforward, Conexões residuais e Layer Normalization.

---

### 02 — Fluxo de dados dentro do Transformer
**Arquivo:** `02-transformer-flow.svg`  
**Seção do diário:** *Como os dados fluem dentro de um bloco Transformer*  

Ilustra o caminho percorrido por um token através das subcamadas:
Atenção → Residual+Norm → Feedforward → Residual+Norm.

---

### 03 — Feedforward Network
**Arquivo:** `03-feedforward.svg`  
**Seção do diário:** *Feedforward Network: refinando representações*  

Explica como a camada MLP aplica transformações não-lineares e
refina os embeddings individualmente para cada posição.

---

### 04 — Conexões Residuais e Normalização
**Arquivo:** `04-residual-norm.svg`  
**Seção do diário:** *Conexões residuais e normalização*  

Mostra como o "atalho" da conexão residual preserva informação
e como a normalização estabiliza o treinamento de redes profundas.

---

### 05 — Pipeline completo do GPT didático
**Arquivo:** `05-gpt-mini-pipeline.svg`  
**Seção do diário:** *Construindo um GPT didático*  

Visualiza a arquitetura completa do modelo, desde a entrada (texto/tokens)
até a saída (probabilidades do próximo token).

---

## 🎨 Diretrizes visuais

Todos os infográficos devem:
- manter consistência visual entre si
- usar cores suaves e profissionais
- evitar excesso de texto
- priorizar leitura rápida em artigos técnicos (Medium / Dev.to)