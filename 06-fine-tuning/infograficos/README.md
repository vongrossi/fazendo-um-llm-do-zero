# Infográficos — Capítulo 06 (Fine-Tuning para Classificação)

Este diretório contém os infográficos utilizados no Capítulo 06 da série:

**Fazendo um LLM do Zero**

Neste capítulo exploramos como adaptar um modelo GPT pré-treinado para resolver tarefas supervisionadas, especificamente classificação de texto.

Os infográficos deste capítulo têm como objetivo ajudar o leitor a visualizar:

- como funciona o fine-tuning
- como um modelo generativo pode ser adaptado para classificação
- como diferentes estratégias de treinamento influenciam o aprendizado
- como funciona o pipeline supervisionado
- como interpretar métricas de avaliação de classificadores

---

## 🎯 Estratégia pedagógica dos infográficos

Os infográficos seguem a progressão conceitual:

```

Pré-Treinamento → Adaptação → Treinamento Supervisionado → Avaliação → Uso Prático

```

Essa progressão acompanha a narrativa do capítulo e prepara o leitor para aplicações reais.

---

## 📊 Lista de Infográficos

```

01-pretrain-vs-finetune.png
02-classification-head.png
03-freeze-vs-unfreeze.png
04-treino-classificacao-pipeline.png
05-metricas-confusion-matrix.png

```

---

## 🧭 Descrição pedagógica de cada infográfico

---

### 01 — Pré-Treinamento vs Fine-Tuning

📍 Seção do diário:
Pré-Treinamento vs Especialização

🎯 Objetivo didático:

Mostrar a diferença entre:

- aprendizado geral da linguagem
- adaptação para tarefas específicas

O infográfico demonstra como o conhecimento adquirido durante o pré-treinamento pode ser reutilizado para novas tarefas.

---

### 02 — Classification Head

📍 Seção do diário:
Transformando um modelo generativo em classificador

🎯 Objetivo didático:

Mostrar como uma camada adicional pode transformar o GPT em classificador.

O infográfico demonstra:

- fluxo de entrada do texto
- processamento pelo modelo GPT
- extração de representação contextual
- camada final de classificação

---

### 03 — Freeze vs Unfreeze

📍 Seção do diário:
Estratégias de Fine-Tuning

🎯 Objetivo didático:

Mostrar diferentes formas de treinar o modelo:

- congelamento completo do backbone
- treinamento parcial
- fine-tuning completo

Este infográfico destaca trade-offs entre custo computacional e capacidade de adaptação.

---

### 04 — Pipeline de Treinamento Supervisionado

📍 Seção do diário:
Pipeline de treinamento para classificação

🎯 Objetivo didático:

Mostrar o fluxo completo do treinamento supervisionado:

- texto rotulado
- tokenização
- processamento pelo GPT
- classificação
- cálculo da loss
- atualização dos pesos

---

### 05 — Métricas e Confusion Matrix

📍 Seção do diário:
Avaliando classificadores de texto

🎯 Objetivo didático:

Mostrar como avaliar modelos de classificação usando:

- accuracy
- precision
- recall
- F1-score
- confusion matrix

Este infográfico ajuda o leitor a interpretar resultados do modelo.

---

## 🎨 Diretrizes Visuais

Todos os infográficos devem manter consistência visual com a série:

✔ Estilo técnico educacional  
✔ Paleta de cores profissional e neutra  
✔ Tipografia moderna e legível  
✔ Uso mínimo de texto  
✔ Ênfase em fluxogramas e diagramas conceituais  
✔ Consistência com capítulos anteriores  
✔ Elementos vetoriais simples  
✔ Destaque visual para fluxos de informação  

