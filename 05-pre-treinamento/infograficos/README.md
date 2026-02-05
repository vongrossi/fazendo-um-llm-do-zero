
# Infográficos — Capítulo 05 (Pré-Treinamento e Geração de Texto)

Este diretório contém os infográficos utilizados no Capítulo 05 da série:

**Fazendo um LLM do Zero**

Neste capítulo exploramos como modelos GPT aprendem linguagem e como geram texto após o treinamento.

Os infográficos deste capítulo têm como objetivo ajudar o leitor a visualizar:

- como funciona o pipeline de treinamento de um LLM
- como a função de perda mede qualidade do modelo
- como ocorre o loop de treinamento
- como diferentes estratégias influenciam geração de texto
- como checkpoints permitem continuidade e reutilização de modelos

---

## 🎯 Estratégia pedagógica dos infográficos

Os infográficos seguem a progressão:

```

Treinamento → Avaliação → Geração → Persistência de Modelos

```

Essa progressão acompanha exatamente a narrativa do capítulo.

---

## 📊 Lista de Infográficos

```

01-pipeline-treinamento.png
02-cross-entropy.png
03-loop-treinamento.png
04-decoding-strategies.png
05-checkpoints.png

```

---

## 🧭 Descrição pedagógica de cada infográfico

---

### 01 — Pipeline de Treinamento de um LLM

📍 Seção do diário:
O pipeline de treinamento de um LLM

🎯 Objetivo didático:

Mostrar o fluxo completo do treinamento:

- Dataset de texto
- Tokenização
- Forward pass no modelo
- Cálculo da loss
- Backpropagation
- Atualização dos pesos

Este infográfico apresenta a visão geral do aprendizado do modelo.

---

### 02 — Cross Entropy e Avaliação Probabilística

📍 Seção do diário:
Cross entropy: medindo o erro probabilístico

🎯 Objetivo didático:

Mostrar como a cross entropy mede o erro do modelo:

- distribuição real do token correto
- distribuição prevista pelo modelo
- comparação entre probabilidades
- interpretação intuitiva da função de perda

---

### 03 — Loop Completo de Treinamento

📍 Seção do diário:
O loop de treinamento completo

🎯 Objetivo didático:

Mostrar o ciclo iterativo do treinamento:

- batches
- forward pass
- cálculo da loss
- backward pass
- atualização do modelo
- epochs

Este infográfico enfatiza repetição e aprendizado gradual.

---

### 04 — Estratégias de Geração de Texto

📍 Seção do diário:
Estratégias de geração de texto

🎯 Objetivo didático:

Comparar diferentes formas de selecionar o próximo token:

- greedy decoding
- temperature sampling
- top-k sampling
- nucleus sampling (top-p)

Este infográfico ajuda a entender como controlamos criatividade e diversidade do modelo.

---

### 05 — Checkpoints e Persistência de Modelos

📍 Seção do diário:
Salvando modelos: checkpoints

🎯 Objetivo didático:

Mostrar como modelos são salvos durante treinamento:

- salvamento periódico de pesos
- retomada de treinamento
- reutilização de modelos
- compartilhamento e reprodutibilidade

---

## 🎨 Diretrizes Visuais

Todos os infográficos devem manter consistência visual com a série:

✔ Estilo técnico educacional  
✔ Paleta de cores neutra e profissional  
✔ Tipografia moderna e legível  
✔ Uso mínimo de texto  
✔ Ênfase em fluxogramas e diagramas conceituais  
✔ Consistência com capítulos anteriores  

---

## 🧩 Convenção de Nome dos Arquivos

Os arquivos devem seguir o padrão:

```

XX-nome-do-conceito.png

```

Exemplo:

```

01-pipeline-treinamento.png

```

---

