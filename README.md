# Fazendo um LLM do Zero 🧠🤖

Este repositório documenta, passo a passo, a construção de um **Large Language Model (LLM) do zero**, com foco em **entendimento fundamental** — e não apenas no uso de APIs prontas.

Aqui, o objetivo **não é criar um concorrente do ChatGPT**, mas compreender profundamente **como LLMs funcionam por dentro**:

- como texto vira número  
- como mecanismos de atenção operam  
- como um modelo do tipo GPT é estruturado  
- como o treinamento molda comportamento  
- e por que tudo isso muda completamente a forma como usamos IA no dia a dia  

Todo o código desta série roda no **Google Colab**, permitindo que qualquer pessoa acompanhe o conteúdo **sem precisar de hardware potente**.

---

## 📚 Estrutura da Série

Cada pasta representa um capítulo da jornada de aprendizado:

```text
00-passo-zero/        → Ambiente, Google Colab, PyTorch e conceitos base
01-o-que-e-um-llm/    → O que é um LLM de verdade
02-texto-vira-numero/ → Tokenização e embeddings
03-atencao/           → Self-attention e multi-head attention
04-gpt-do-zero/       → Construindo um GPT do zero
05-treinamento/       → Treinamento, loss e geração de texto
06-fine-tuning/       → Ajustando comportamento do modelo
07-instruction-tuning → Modelos que seguem instruções
```

---

## ☁️ Por que Google Colab?

O Google Colab é a base prática deste projeto porque:

* elimina a necessidade de setup local
* oferece CPU/GPU sob demanda
* garante reprodutibilidade dos experimentos
* permite executar os notebooks com **um único clique**

Isso torna o aprendizado mais acessível, focando no **entendimento dos conceitos**, e não em infraestrutura.

---

## 📦 O que você vai encontrar em cada capítulo

Cada capítulo da série contém:

* 📖 um **roteiro em Markdown** (origem do post no Medium)
* 🧪 um **notebook executável**
* 📊 **infográficos didáticos** para visualização dos conceitos
* 🔗 **links diretos para abrir o notebook no Google Colab**

---

## 📘 Referência

Este projeto é inspirado no livro
**Build a Large Language Model (From Scratch)**, de *Sebastian Raschka*,
adaptando os conceitos para uma abordagem didática em **português** e execução prática no **Google Colab**.

---

## ⚠️ Aviso honesto

Este é um projeto **educacional**.

Os modelos construídos aqui são pequenos e didáticos, mas utilizam **os mesmos princípios fundamentais** empregados em grandes modelos de produção.

O foco é construir **modelo mental**, não escalar para bilhões de parâmetros.
