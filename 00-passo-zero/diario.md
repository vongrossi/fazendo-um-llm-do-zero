# Passo Zero: antes de criar um LLM, precisamos alinhar o terreno

Antes de falar sobre tokens, atenção ou modelos, precisamos resolver um problema real:
**como aprender LLMs sem depender de hardware caro?**

A resposta prática para essa série é: **Google Colab**.

---

## ☁️ O que é o Google Colab?

O Google Colab é um ambiente de notebooks (estilo Jupyter) rodando na nuvem.
Você escreve Python em células, executa e vê os resultados em sequência.

O diferencial aqui é o “zero fricção”:
- você não precisa instalar nada no seu computador
- consegue usar CPU/GPU com poucos cliques
- o notebook vira um laboratório replicável

> Ideia-chave: Colab tira o peso da infraestrutura e coloca o foco no entendimento.

![O que é o Colab](./infograficos/00-o-que-e-colab.png)

---

## ✅ Por que vamos usar o Colab nesta série?

Porque ele:
- democratiza o acesso (não precisa de GPU local)
- torna o estudo reproduzível (mesma base para todo mundo)
- facilita experimentação rápida (testar, errar, ajustar, entender)
- funciona muito bem para **modelos pequenos e didáticos**

---

## ⚠️ Limitações do Colab (honestidade importa)

O Colab não é um datacenter gratuito infinito.

Algumas limitações:
- a sessão pode expirar
- a GPU nem sempre está disponível (depende do plano e do momento)
- não é ambiente de produção

Mas… para aprender LLMs do zero, ele é perfeito.

---

## 🔥 O que é PyTorch?

PyTorch é uma biblioteca de deep learning usada para construir e treinar redes neurais.

Ele dá as peças principais:
- **tensores** (números com “forma”: vetores, matrizes, etc.)
- operações rápidas (CPU/GPU)
- cálculo automático de gradientes (base do treinamento)

Se LLM é “texto virando matemática”, PyTorch é a oficina onde a matemática acontece.

![Visão geral do PyTorch](./infograficos/01-pytorch-visao-geral.png)

---

## 📦 O que são bibliotecas em Python?

Bibliotecas são “caixas de ferramentas”.
Em vez de escrever tudo do zero, você importa ferramentas prontas e confiáveis.

Exemplo:

```python
import torch
```

Essa linha carrega um ecossistema inteiro de funções e classes.
Para instalar bibliotecas, usamos o pip:

```bash
pip install nome-da-biblioteca
```

### 🧪 Código: seu primeiro contato com PyTorch

A ideia aqui é simples:
 - criar um tensor
 - fazer uma operação
 - enxergar a saída


```python
import torch

x = torch.tensor([1.0, 2.0, 3.0])
y = x * 2

print("x =", x)
print("y =", y)
```

Isso pode parecer bobo, mas é um marco:
daqui pra frente, texto vira número, e número vira tensor.

### 🧠 O que isso muda na forma de aprender LLMs?

Quando você entende o básico:
- “inteligência” vira processo
- “mágica” vira engenharia
- “prompt” vira interface, não fundamento

E aí você começa a usar LLMs melhor:
- com mais consciência de limitações
- com melhores estratégias
- com mais capacidade de depurar problemas

Run it now
 - Notebook: 00-passo-zero/notebook.ipynb
 - Abrir direto no Colab: (veja links.md)

