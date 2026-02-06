# Infográficos — Capítulo 06: Fine-Tuning para Classificação

Este diretório contém os infográficos utilizados no Capítulo 06 da série
**Fazendo um LLM do Zero**.

Neste capítulo exploramos como adaptar um modelo GPT pré-treinado para resolver
tarefas supervisionadas, especificamente classificação de texto.

Os infográficos deste capítulo ajudam a visualizar:
- a diferença entre pré-treinamento e fine-tuning
- a adaptação de um modelo generativo para classificação
- estratégias de treinamento (congelamento vs ajuste total)
- pipeline de treinamento supervisionado
- métricas de avaliação de classificadores

---

## 📊 Lista de Infográficos do Capítulo

### 01 — Pré-Treinamento vs Fine-Tuning
**Arquivo:** `01-pretrain-vs-finetune.svg`  
**Seção do diário:** *Pré-Treinamento vs Especialização*  

Demonstra a diferença conceitual entre aprender linguagem de forma geral
e especializar o modelo para uma tarefa específica.

---

### 02 — Classification Head
**Arquivo:** `02-classification-head.svg`  
**Seção do diário:** *Classification Head*  

Mostra como substituir a cabeça de modelagem de linguagem por uma camada
linear simples para classificar o texto processado.

---

### 03 — Freeze vs Unfreeze
**Arquivo:** `03-freeze-vs-unfreeze.svg`  
**Seção do diário:** *Congelamento de Camadas*  

Ilustra as estratégias de treinar apenas a cabeça (congelar backbone)
ou treinar o modelo todo, destacando trade-offs de custo e performance.

---

### 04 — Pipeline de treinamento supervisionado
**Arquivo:** `04-treino-classificacao-pipeline.svg`  
**Seção do diário:** *Pipeline de treinamento para classificação*  

Visualiza o fluxo completo: Texto Rotulado → Tokenização → GPT → Classificação
→ Cálculo de Loss Supervisionada → Atualização de Pesos.

---

### 05 — Métricas e Confusion Matrix
**Arquivo:** `05-metricas-confusion-matrix.svg`  
**Seção do diário:** *Avaliando classificadores de texto*  

Explica visualmente como interpretar Accuracy, Precision, Recall, F1-Score
e a Matriz de Confusão para avaliar a qualidade do modelo.

---

## 🎨 Diretrizes visuais

Todos os infográficos devem:
- manter consistência visual entre si
- usar cores suaves e profissionais
- evitar excesso de texto
- priorizar leitura rápida em artigos técnicos (Medium / Dev.to)