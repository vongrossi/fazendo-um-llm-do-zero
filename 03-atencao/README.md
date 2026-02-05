# Capítulo 03 — Atenção (Self-Attention)

Se o capítulo anterior respondeu **como texto vira números**,  
este capítulo responde a pergunta que mudou completamente a história dos modelos de linguagem:

**Como o modelo decide quais partes do contexto são importantes?**

Aqui nasce o mecanismo que tornou possíveis os Transformers modernos e, consequentemente, os LLMs atuais.

---

## 🎯 Objetivo do Capítulo

Ao final deste capítulo, você deve ser capaz de:

- entender por que modelos precisam de mecanismos para lidar com contexto global
- explicar intuitivamente o que é atenção
- compreender como vetores de contexto são calculados
- entender o papel das matrizes Query, Key e Value (Q, K, V)
- explicar o que é máscara causal e por que ela é essencial para modelos autoregressivos
- compreender por que multi-head attention melhora a capacidade do modelo
- visualizar como o módulo de atenção se encaixa dentro de um Transformer

Este capítulo marca a transição entre **preparação de dados** e **arquitetura neural real**.

---

## 🧭 Como este capítulo está organizado

O conteúdo segue uma progressão do intuitivo para o técnico:

### 1. O problema do contexto
- Por que linguagem não pode ser processada palavra por palavra
- Dependências de longo alcance

### 2. Intuição da atenção
- Atenção como ponderação de importância
- Vetores de contexto como médias ponderadas

### 3. Self-Attention básico
- Cálculo de pesos de atenção
- Normalização via softmax
- Construção do vetor de contexto

### 4. Query, Key e Value
- Projeções treináveis
- Representação flexível do contexto

### 5. Self-attention com pesos treináveis
- Aprendizado automático de relações linguísticas
- Construção do mecanismo usado em Transformers

### 6. Máscara causal
- Restrição de acesso ao futuro
- Base do treinamento autoregressivo

### 7. Multi-head attention
- Atenção paralela
- Captura de múltiplos tipos de relações semânticas

### 8. Atenção dentro do Transformer
- Como o módulo de atenção se conecta ao restante da arquitetura GPT-like

Cada seção é acompanhada por infográficos e implementações progressivas em código.

---

## 🧪 Parte prática (notebook)

Este capítulo inclui um notebook executável no Google Colab que implementa, passo a passo:

- mecanismo de atenção simplificado
- cálculo de pesos de atenção
- implementação de Q, K e V
- aplicação de máscara causal
- implementação conceitual de multi-head attention

O foco é **entendimento profundo do mecanismo**, não otimização ou performance.

---

## 📊 Infográficos

Este capítulo utiliza infográficos para ilustrar:

- por que contexto global é necessário
- funcionamento intuitivo da atenção
- cálculo de vetores de contexto
- projeções Q, K e V
- máscara causal
- multi-head attention
- posição do módulo de atenção dentro do Transformer

Os detalhes e prompts dos infográficos estão documentados em:

- `infograficos/README.md`

---

## ▶️ Como executar

1. Leia o diário do capítulo:
   - `diario.md`

2. Execute o notebook:
   - `notebook.ipynb`

3. Ou abra diretamente no Google Colab:
   - veja os links em `links.md`

---


## 🎥 Material complementar

Este capítulo é fortemente baseado nas explicações do próprio autor do livro, que aprofunda visualmente o mecanismo de atenção:

- Vídeo: *Self-Attention Explained* — Sebastian Raschka

O vídeo reforça a intuição e complementa a implementação apresentada neste capítulo.

---

## 📘 Referência

Este capítulo é baseado no Capítulo 3 do livro  
**Build a Large Language Model (From Scratch)** — Sebastian Raschka.

O conteúdo foi adaptado para:

- abordagem didática em português
- execução prática no Google Colab
- foco em construção conceitual progressiva
- visualização detalhada dos mecanismos internos do Transformer

---

## ⚠️ Observação importante

Self-attention é o núcleo matemático e arquitetural dos LLMs modernos.

Este capítulo é naturalmente mais técnico e exige leitura cuidadosa.

Entretanto, dominar atenção permite compreender:

- Transformers
- GPT
- BERT
- Modelos multimodais
- Arquiteturas modernas de IA generativa

Este é o ponto onde a “caixa preta” começa a se abrir.


