# Capítulo 04 — Construindo um GPT do Zero

Nos capítulos anteriores, construímos a base conceitual dos LLMs:

- Capítulo 01 — O que é um LLM  
- Capítulo 02 — Como texto vira números  
- Capítulo 03 — Como atenção cria contexto  

Agora chegamos ao momento onde tudo se conecta:

> Neste capítulo vamos construir, passo a passo, um modelo GPT funcional.

Aqui o objetivo não é criar um modelo gigante de produção, mas sim entender profundamente **como a arquitetura GPT funciona internamente**.

---

## 🎯 Objetivo do Capítulo

Ao final deste capítulo, você deverá ser capaz de:

- entender como um bloco Transformer é estruturado
- compreender o papel das conexões residuais e da normalização
- implementar feedforward networks dentro de Transformers
- montar um GPT didático usando PyTorch
- entender o fluxo completo: tokens → embeddings → atenção → saída
- implementar geração autoregressiva simples
- visualizar como teoria e código se conectam

Este capítulo representa a transição entre **entender os mecanismos** e **construir um modelo real**.

---

## 🧭 Como este capítulo está organizado

O conteúdo segue uma progressão pedagógica do conceitual para o prático:

---

### 1. Revisão rápida da pipeline de um LLM

Revisamos os componentes que já aprendemos:

- Tokenização
- Embeddings
- Self-Attention
- Máscara causal

Essa seção prepara o leitor para entender como esses elementos serão combinados dentro de um GPT.

---

### 2. Estrutura de um Bloco Transformer

Aqui apresentamos o coração da arquitetura GPT:

- Self-Attention
- Feedforward Network
- Conexões residuais
- Layer Normalization

O objetivo é mostrar como esses componentes trabalham juntos para construir representações contextuais profundas.

---

### 3. Feedforward Network dentro do Transformer

Explicamos:

- por que uma rede feedforward é aplicada após a atenção
- como ela introduz não-linearidade
- como cada posição da sequência é refinada independentemente

---

### 4. Conexões Residuais e Normalização

Mostramos por que Transformers conseguem ser empilhados em grande profundidade:

- conexões residuais preservam informação
- normalização estabiliza o treinamento
- juntos, permitem escalabilidade

---

### 5. Construindo um GPT Didático

Nesta seção, implementamos:

- Bloco Transformer completo
- Empilhamento de blocos
- Cabeça de saída para previsão de tokens
- Pipeline completo do modelo

---

### 6. Geração Autoregressiva

Mostramos como o modelo gera texto:

- previsão do próximo token
- loop de geração
- amostragem simples

---

### 7. Limitações e Escalabilidade

Discutimos:

- por que o modelo didático é pequeno
- diferenças para modelos reais
- otimizações usadas em produção
- preparação para o capítulo de treinamento

---

## 🧪 Parte prática (notebook)

Este capítulo inclui um notebook executável no Google Colab que implementa:

- classe Self-Attention com máscara causal
- classe FeedForward
- classe TransformerBlock
- modelo GPTMini completo
- treinamento em dataset simples
- geração autoregressiva de texto

O notebook prioriza clareza conceitual e explicações linha a linha.

---

## 📊 Infográficos

Este capítulo utiliza infográficos para explicar:

- estrutura do bloco Transformer
- fluxo de dados com conexões residuais
- funcionamento do feedforward
- papel da normalização
- pipeline completo de um GPT didático

Os detalhes dos infográficos estão documentados em:

infograficos/README.md


---

## ▶️ Como executar

1. Leia o diário do capítulo:


diario.md


2. Execute o notebook:

notebook.ipynb


3. Ou abra diretamente no Google Colab:


veja links.md


---

## 🎥 Material complementar

Este capítulo é inspirado na implementação e explicações do próprio autor do livro, que demonstra a construção progressiva de um GPT:

Vídeo:
Building a GPT from Scratch — Sebastian Raschka

O vídeo complementa o material deste capítulo, mas o foco aqui é fornecer uma explicação detalhada e interativa com código comentado.

---

## 📘 Referência

Este capítulo é baseado no Capítulo 4 do livro:

**Build a Large Language Model (From Scratch)**  
Sebastian Raschka

O conteúdo foi adaptado para:

- abordagem didática em português
- execução prática no Google Colab
- foco em entendimento estrutural da arquitetura GPT
- conexão entre teoria e implementação

---

## ⚠️ Observação importante

Este capítulo marca o ponto onde a arquitetura Transformer começa a ser implementada como um modelo funcional.

É normal que o conteúdo seja mais técnico que os capítulos anteriores.

Entretanto, dominar este capítulo permite compreender:

- como GPT realmente funciona
- como modelos generativos produzem texto
- como frameworks modernos implementam Transformers
- como evoluir para modelos maiores e treinamento real

Este é o momento onde o leitor deixa de apenas estudar LLMs e começa a construí-los.
