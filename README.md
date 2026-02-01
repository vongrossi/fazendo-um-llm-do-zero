# 🧠 Fazendo um LLM do Zero (Home-Made LLM)

Este repositório é o registro de estudos do projeto **"Fazer um LLM do Zero"**. Funciona como meu diário de bordo técnico; a ideia é abrir a caixa preta e entender como os Large Language Models (LLMs) realmente funcionam "embaixo do capô".

O modelo é baseado na arquitetura do **GPT**, utilizando apenas **PyTorch** e o seu core.

> **"Existe uma diferença brutal entre apenas saber chamar uma API e entender exatamente o que está sendo processado entre o seu request e a resposta que chega. Este projeto é sobre fechar esse buraco e entender o fluxo real dos dados."**

---

## 🚀 O Projeto & Missão
Este guia é integralmente baseado na obra de referência da área:
* **Livro:** [Build a Large Language Model (from Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch) - Sebastian Raschka.
* **Repositório Oficial:** [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch).

**Minha Visão do projeto:** Traduzir este conhecimento complexo e extremamente importante dado o momomento que estamos para o Português e torná-lo acessível. 
- **Sem Barreiras de Hardware**: Todo o código é projetado para rodar no **Google Colab (GPU Gratuita)**, garantindo que o hardware não seja um bloqueio para o aprendizado de ponta.
- **Componentes por Módulo**: Construção passo a passo, do tratamento de dados ao ajuste fino (fine-tuning).

---

## 🗺️ Roadmap de Desenvolvimento (Baseado no Livro)

Seguiremos a estrutura de capítulos para garantir uma base sólida:

| Capítulo | Status | Descrição | Guia / Blog |
| :--- | :--- | :--- | :--- |
| **01. Intro** | ✅ | Anatomia dos LLMs e pipeline de treinamento. | [Post #1](docs/post_01.md) |
| **02. Dados** | ⏳ | Tokenização (BPE), Data Loaders e Embeddings. | [Em breve] |
| **03. Atenção** | ⏳ | Mecanismos de Attention (Self, Causal, Multi-head). | [Em breve] |
| **04. Arquitetura** | ⏳ | Implementando o GPT: blocos Transformer e Camadas. | [Em breve] |
| **05. Pré-treino** | ⏳ | Otimização, perda (loss) e carregamento de pesos. | [Em breve] |
| **06. Tuning I** | ⏳ | Fine-tuning para Classificação (Spam/Sentimentos). | [Em breve] |
| **07. Tuning II** | ⏳ | Fine-tuning para Instruções (Assistente de Chat). | [Em breve] |

---

## 🛠️ Tecnologias 
* **Linguagem:** Python 3.10+
* **Framework:** PyTorch (Core/Puro)
* **Tokenização:** Tiktoken (OpenAI - Byte Pair Encoding)
* **Ambiente de Execução:** Google Colab / Jupyter Notebooks

---

## 📂 Organização do Repositório
* `/notebooks`: Arquivos `.ipynb` detalhados e compatíveis com Google Colab.
* `/src`: Módulos Python reutilizáveis (o "engine" modular do LLM).
* `/docs`: Documentação técnica e rascunhos para os artigos explicativos.
* `/data`: Amostras de datasets para testes (ex: TinyShakespeare).

---

## 📜 Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---
*Criado com ☕ por **vongrossi** como parte de um estudo profundo sobre Inteligência Artificial.*