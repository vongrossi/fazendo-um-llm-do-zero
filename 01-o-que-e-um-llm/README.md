# Capítulo 01 — O que é um LLM (de verdade)

Este capítulo estabelece o **modelo mental fundamental** para todo o restante da série.

Antes de falar sobre tokenização, atenção ou treinamento, precisamos responder com clareza:
**o que é — e o que não é — um Large Language Model (LLM).**

Aqui, o foco não é hype nem atalhos.
É entendimento conceitual sólido.

---

## 🎯 Objetivo do Capítulo

Ao final deste capítulo, você deve ser capaz de:

- explicar o que é um LLM sem recorrer a frases vagas ou mágicas
- entender por que “prever o próximo token” é o coração do modelo
- reconhecer por que LLMs geram tantos tipos diferentes de aplicações
- compreender os estágios de construção e uso de um LLM
- ter uma visão de alto nível da arquitetura Transformer
- entender o que diferencia um modelo GPT de outras arquiteturas
- saber o que são tokens, modelos fundacionais, encoder e decoder

Este capítulo **não implementa um LLM completo**.
Ele constrói o **mapa conceitual** que torna os próximos capítulos compreensíveis.

---

## 🧭 Como este capítulo está organizado

O conteúdo é apresentado em camadas, seguindo uma progressão lógica:

1. **O que é um LLM**
   - LLM como modelo probabilístico
   - Previsão do próximo token
   - Analogias do mundo real

2. **Aplicações de LLMs**
   - Por que um único mecanismo gera tantos usos diferentes
   - Texto, código, resumo, perguntas e respostas

3. **Estágios de construção e uso**
   - Dados
   - Pré-treinamento
   - Ajuste (fine-tuning)
   - Uso em aplicações

4. **Introdução à arquitetura Transformer**
   - Por que arquiteturas anteriores não escalam bem
   - Atenção como mecanismo central
   - Processamento em paralelo

5. **Um olhar mais próximo do GPT**
   - GPT como Transformer do tipo *decoder-only*
   - Geração autoregressiva
   - Relação com modelos fundacionais

6. **Conceitos fundamentais**
   - Token
   - Modelo fundacional
   - Encoder
   - Decoder

Cada seção é acompanhada de **infográficos didáticos** e exemplos conceituais.

---

## 🧪 Parte prática (notebook)

Este capítulo inclui um notebook executável no Google Colab com um exemplo prático que:

- demonstra a ideia de previsão do próximo token
- mostra como comportamento “inteligente” emerge de regras simples
- antecipa conceitos que serão aprofundados nos próximos capítulos

O objetivo do notebook **não é performance**, mas compreensão.

---

## 📊 Infográficos

Este capítulo utiliza infográficos para reforçar visualmente conceitos como:

- LLM como preditor de tokens
- Ciclo de vida de um LLM
- Arquitetura Transformer em alto nível
- Diferença entre encoder e decoder
- Estrutura conceitual de um modelo GPT

As descrições dos infográficos estão documentadas no arquivo:

- `infograficos/README.md`

---

## ▶️ Como executar

1. Leia o diário do capítulo:
   - `diario.md`

2. Execute o notebook:
   - `notebook.ipynb`

3. Ou abra diretamente no Google Colab:
   - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vongrossi/fazendo-um-llm-do-zero/blob/main/01-o-que-e-um-llm/notebook.ipynb)
   - ou veja mais detalhes em `links.md`

---

## 📘 Referências

Este capítulo é baseado no Capítulo 1 do livro  
*Build a Large Language Model (From Scratch)*, de Sebastian Raschka,

e em materiais complementares do próprio autor, incluindo palestras introdutórias sobre LLMs.

O conteúdo foi adaptado para:
- uma abordagem didática em português
- execução prática no Google Colab
- foco em modelo mental, não apenas implementação

---

## ⚠️ Observação importante

Se algum conceito parecer abstrato neste capítulo, isso é esperado.

Os próximos capítulos transformam cada ideia apresentada aqui em:
- código
- experimentos
- visualizações
- implementações progressivas

Este capítulo é o **mapa**.
Os próximos são o **território**.
