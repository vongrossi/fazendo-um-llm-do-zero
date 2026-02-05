# Infográficos — Capítulo 04 (Construindo um GPT do Zero)

Este diretório contém os infográficos utilizados no Capítulo 04 da série:

**Fazendo um LLM do Zero**

Este capítulo marca a transição entre compreender os componentes individuais dos Transformers e construir um modelo GPT completo.

Os infográficos deste capítulo têm como objetivo ajudar o leitor a visualizar:

- como um bloco Transformer é estruturado
- como o fluxo de dados ocorre dentro do modelo
- como feedforward complementa a atenção
- como conexões residuais e normalização estabilizam o treinamento
- como o pipeline completo de um GPT funciona

---

## 🎯 Estratégia pedagógica dos infográficos

Os infográficos seguem a progressão:

Arquitetura → Fluxo → Componentes → Pipeline completo


Essa progressão acompanha exatamente a narrativa do capítulo.

---

## 📊 Lista de Infográficos

01-transformer-block.png
02-transformer-flow.png
03-feedforward.png
04-residual-norm.png
05-gpt-mini-pipeline.png


---

## 🧭 Descrição pedagógica de cada infográfico

---

### 01 — Estrutura de um Bloco Transformer

📍 Seção do diário:
O bloco fundamental do Transformer

🎯 Objetivo didático:

Mostrar visualmente os quatro componentes principais de um bloco Transformer:

- Self-Attention
- Feedforward Network
- Conexão residual
- Layer Normalization

Este infográfico apresenta a arquitetura estrutural do bloco.

---

### 02 — Fluxo de dados dentro do Transformer

📍 Seção do diário:
Como os dados fluem dentro de um bloco Transformer

🎯 Objetivo didático:

Mostrar como um token percorre as etapas do bloco:

- Entrada
- Atenção
- Residual + Normalização
- Feedforward
- Residual + Normalização
- Saída

Este infográfico foca no fluxo computacional.

---

### 03 — Feedforward Network

📍 Seção do diário:
Feedforward Network: refinando representações

🎯 Objetivo didático:

Explicar como a rede feedforward:

- aplica transformação não-linear
- expande e comprime dimensionalidade
- refina embeddings individualmente por posição

---

### 04 — Conexões Residuais e Layer Normalization

📍 Seção do diário:
Conexões residuais e normalização

🎯 Objetivo didático:

Mostrar como:

- conexões residuais preservam informação
- normalização estabiliza treinamento
- ambos permitem empilhamento profundo de camadas

---

### 05 — Pipeline completo de um GPT didático

📍 Seção do diário:
Construindo um GPT didático

🎯 Objetivo didático:

Mostrar o fluxo completo:

Texto → Tokens → Embeddings → Blocos Transformer → Saída de probabilidades

Este infográfico fecha o capítulo e conecta todos os conceitos anteriores.

---

