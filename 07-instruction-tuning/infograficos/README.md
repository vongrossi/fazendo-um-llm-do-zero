
# Infográficos — Capítulo 07 (Instruction Tuning)

Este diretório contém os infográficos utilizados no Capítulo 07 da série:

**Fazendo um LLM do Zero**

Neste capítulo exploramos como transformar modelos de linguagem em assistentes capazes de seguir instruções humanas.

Os infográficos deste capítulo têm como objetivo ajudar o leitor a visualizar:

- como modelos base evoluem para modelos alinhados
- como datasets de instruções são estruturados
- como funciona o mascaramento de loss em tarefas conversacionais
- como ocorre o pipeline de supervised fine-tuning
- como modelos conversacionais são avaliados

---

## 🎯 Estratégia pedagógica dos infográficos

Os infográficos seguem a progressão conceitual final da série:

```

Modelo Base → Instruction Tuning → Treinamento Supervisionado → Avaliação Conversacional

```

Essa progressão representa o fechamento da jornada de construção de LLMs apresentada na série.

---

## 📊 Lista de Infográficos

```

01-instruction-tuning-visao-geral.png
02-formato-dados-instrucao.png
03-mascaramento-loss-resposta.png
04-pipeline-sft.png
05-avaliacao-respostas.png

```

---

## 🧭 Descrição pedagógica de cada infográfico

---

### 01 — Instruction Tuning: Visão Geral

📍 Seção do diário:
Do Modelo Base ao Assistente Conversacional

🎯 Objetivo didático:

Mostrar a evolução de modelos de linguagem para modelos alinhados ao comportamento humano.

O infográfico demonstra:

- modelo pré-treinado com conhecimento geral
- processo de instruction tuning
- modelo especializado em seguir instruções

---

### 02 — Estrutura de Dados para Instruções

📍 Seção do diário:
Estrutura de Dados para Instruction Tuning

🎯 Objetivo didático:

Mostrar como datasets conversacionais são estruturados.

O infográfico demonstra:

- instruction
- input opcional
- response
- estrutura padronizada de prompts

---

### 03 — Mascaramento da Loss

📍 Seção do diário:
Mascaramento da Loss

🎯 Objetivo didático:

Mostrar como o treinamento supervisionado foca apenas na resposta do modelo.

O infográfico demonstra:

- tokens da instrução usados como contexto
- tokens da resposta usados para cálculo da loss
- impacto do masking no aprendizado do modelo

---

### 04 — Pipeline de Supervised Fine-Tuning (SFT)

📍 Seção do diário:
Pipeline de SFT

🎯 Objetivo didático:

Mostrar o fluxo completo do instruction tuning.

O infográfico demonstra:

- dataset de instruções
- tokenização estruturada
- reutilização de pesos pré-treinados
- treinamento supervisionado
- atualização do modelo

---

### 05 — Avaliação de Respostas Conversacionais

📍 Seção do diário:
Avaliando Modelos Conversacionais

🎯 Objetivo didático:

Mostrar como respostas geradas por modelos são avaliadas.

O infográfico demonstra:

- comparação qualitativa de respostas
- critérios de avaliação
- limitações de métricas tradicionais
- importância da avaliação humana

---

## 🎨 Diretrizes Visuais

Todos os infográficos devem manter consistência visual com a série:

✔ Estilo técnico educacional  
✔ Paleta profissional e neutra  
✔ Tipografia moderna e legível  
✔ Uso mínimo de texto  
✔ Ênfase em fluxos conceituais  
✔ Consistência com capítulos anteriores  
✔ Elementos vetoriais simples  
✔ Destaque visual para interações humanas e comportamento do modelo  

---

## 🧩 Convenção de Nome dos Arquivos

Os arquivos devem seguir o padrão:

```

XX-nome-do-conceito.png

```

Exemplo:

```

01-instruction-tuning-visao-geral.png

```

