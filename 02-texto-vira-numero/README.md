# Capítulo 02 — Texto vira número

Se o capítulo anterior respondeu **o que é um LLM**,  
este capítulo responde uma pergunta ainda mais fundamental:

**como texto vira algo que um modelo consegue processar?**

Aqui começa, de fato, a construção técnica de um modelo de linguagem.

---

## 🎯 Objetivo do Capítulo

Ao final deste capítulo, você deve ser capaz de:

- entender por que modelos não processam texto bruto
- explicar o papel dos embeddings em modelos de linguagem
- compreender o que é tokenização e por que ela é necessária
- saber como um vocabulário é construído
- entender a diferença entre texto, tokens e token IDs
- explicar como funcionam encode e decode
- compreender como modelos lidam com palavras desconhecidas (BPE)
- entender o conceito de janela deslizante e pares input–target
- visualizar o pipeline completo de entrada de um modelo GPT-like

Este capítulo **não treina um Transformer ainda**.
Ele constrói toda a **infraestrutura conceitual e prática** que torna isso possível.

---

## 🧭 Como este capítulo está organizado

O conteúdo segue uma progressão lógica, do mais intuitivo ao mais técnico:

1. **Por que texto não pode ser usado diretamente**
   - Dados simbólicos vs dados numéricos
   - Texto, áudio e vídeo como entrada bruta

2. **Embeddings: representando significado como números**
   - Vetores como representação
   - Similaridade no espaço vetorial

3. **Tokenização**
   - Tokens não são palavras
   - Construção de vocabulário
   - Token IDs

4. **Encode e Decode**
   - Texto → números
   - Números → texto

5. **Lidando com palavras desconhecidas**
   - Problema de OOV (out-of-vocabulary)
   - Byte Pair Encoding (BPE)
   - Subwords

6. **Janela deslizante e pares input–target**
   - Como o modelo aprende a prever o próximo token
   - Máscara causal

7. **Pipeline completo de entrada do GPT**
   - Texto → tokens → IDs → embeddings → embeddings posicionais

Cada seção é acompanhada de **infográficos didáticos** e exemplos práticos.

---

## 🧪 Parte prática (notebook)

Este capítulo inclui um notebook executável no Google Colab que:

- implementa um tokenizer simples
- constrói um vocabulário a partir de texto
- converte texto em token IDs
- cria pares input–target usando janela deslizante
- conecta o pipeline completo de entrada de um modelo GPT-like

O foco do notebook é **clareza conceitual**, não performance.

---

## 📊 Infográficos

Este capítulo utiliza infográficos para visualizar conceitos como:

- conversão de texto em vetores
- espaço vetorial e similaridade semântica
- tokenização e vocabulário
- encode e decode
- tokenização por subwords (BPE)
- janela deslizante
- pipeline de entrada de um modelo GPT-like

As descrições dos infográficos estão documentadas em:

- [infograficos/README.md](infograficos/README.md)

---

## ▶️ Como executar

1. Leia o diário do capítulo:
   - [diario.md](diario.md)

2. Execute o notebook:
   - [notebook.ipynb](notebook.ipynb)

3. Ou abra diretamente no Google Colab:
   - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vongrossi/fazendo-um-llm-do-zero/blob/main/02-texto-vira-numero/notebook.ipynb)
   - ou veja mais detalhes em [links.md](links.md)

---

## 🎥 Material complementar

Este capítulo é fortemente inspirado no conteúdo do próprio autor do livro,
que aprofunda visualmente os conceitos de tokenização e embeddings:


---

## 📘 Referência

Este capítulo é baseado no Capítulo 2 do livro  
*Build a Large Language Model (From Scratch)*, de Sebastian Raschka.

O conteúdo foi adaptado para:
- uma abordagem didática em português
- execução prática no Google Colab
- foco em entendimento profundo, não apenas uso de bibliotecas prontas

---

## ⚠️ Observação importante

Se este capítulo parecer denso, isso é intencional.

Tokenização e embeddings são conceitos que:
- aparecem em todos os LLMs
- impactam desempenho, custo e qualidade
- influenciam diretamente como o modelo aprende

Entender bem este capítulo economiza muita confusão nos próximos.
