# Infográficos — Capítulo 07: Instruction Tuning

Este diretório contém os infográficos utilizados no Capítulo 07 da série
**Fazendo um LLM do Zero**.

Neste capítulo exploramos como transformar modelos de linguagem em assistentes
capazes de seguir instruções humanas.

Os infográficos deste capítulo ajudam a visualizar:
- como modelos base evoluem para modelos alinhados
- a estrutura de dados para instruction tuning
- o mascaramento de loss (focando apenas na resposta)
- o pipeline de Supervised Fine-Tuning (SFT)
- avaliação qualitativa de modelos conversacionais

---

## 📊 Lista de Infográficos do Capítulo

### 01 — Instruction Tuning: Visão Geral
**Arquivo:** `01-instruction-tuning-visao-geral.png`  
**Seção do diário:** *Do Modelo Base ao Assistente Conversacional*  

Demonstra a evolução de um modelo pré-treinado (que apenas completa texto)
para um modelo especializado em interagir e seguir comandos.

### 02 — Estrutura de dados para instruções
**Arquivo:** `02-formato-dados-instrucao.png`  
**Seção do diário:** *Estrutura de Dados para Instruction Tuning*  

Mostra os componentes de um dataset conversacional: Instrução, Input (opcional)
e Resposta, formatados em um formato estruturado.

### 03 — Mascaramento da Loss
**Arquivo:** `03-mascaramento-loss-resposta.png`  
**Seção do diário:** *Mascaramento da Loss*  

Ilustra como a loss é calculada apenas sobre os tokens da resposta,
usando a instrução apenas como contexto, para focar o aprendizado.

### 04 — Pipeline de SFT
**Arquivo:** `04-pipeline-sft.png`  
**Seção do diário:** *Pipeline de Supervised Fine-Tuning (SFT)*  

Visualiza o fluxo completo: Dataset de Instruções → Tokenização Estruturada
→ Reutilização de Pesos → Treino Supervisionado → Modelo Alinhado.

### 05 — Avaliação de respostas
**Arquivo:** `05-avaliacao-respostas.png`  
**Seção do diário:** *Avaliando Modelos Conversacionais*  

Apresenta critérios qualitativos para julgar se o modelo segue instruções,
é coerente e útil, contrastando com métricas puramente numéricas.

---

## 🎨 Diretrizes visuais

Todos os infográficos devem:
- manter consistência visual entre si
- usar cores suaves e profissionais
- evitar excesso de texto
- priorizar leitura rápida em artigos técnicos (Medium / Dev.to)