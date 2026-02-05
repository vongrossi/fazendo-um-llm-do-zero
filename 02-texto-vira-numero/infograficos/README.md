# Infográficos — Capítulo 02: Texto vira número

Este diretório contém os infográficos utilizados no Capítulo 02 da série
**Fazendo um LLM do Zero**.

Este capítulo é visualmente mais denso porque introduz os conceitos
mais fundamentais de toda a pipeline de modelos de linguagem:
tokenização, embeddings e preparação de dados.

Os infográficos aqui têm como objetivo:
- reduzir abstração matemática
- criar intuição visual
- conectar texto simbólico com representação numérica
- preparar o leitor para atenção e Transformers

---

## 📊 Lista de Infográficos do Capítulo

### 01 — Texto bruto → Vetor numérico
**Arquivo:** `01-texto-para-vetor.png`  
**Seção do diário:** *Por que texto não pode ser usado diretamente*  

Mostra como texto, áudio e vídeo são convertidos em vetores numéricos
por meio de modelos de embedding.

---

### 02 — Espaço vetorial e similaridade semântica
**Arquivo:** `02-espaco-vetorial.png`  
**Seção do diário:** *Embeddings: representando significado como números*  

Ilustra como conceitos semanticamente semelhantes aparecem próximos
em um espaço vetorial.

---

### 03 — Tokenização e construção do vocabulário
**Arquivo:** `03-tokenizacao-vocabulario.png`  
**Seção do diário:** *Tokenização: quebrando texto em unidades processáveis*  

Mostra o processo de tokenizar texto, remover duplicatas
e mapear tokens para IDs numéricos.

---

### 04 — Encode e Decode
**Arquivo:** `04-encode-decode.png`  
**Seção do diário:** *Encode e Decode: texto ↔ números*  

Ilustra as duas operações fundamentais que conectam humanos e modelos:
converter texto em números e números de volta em texto.

---

### 05 — BPE e subwords
**Arquivo:** `05-bpe-subwords.png`  
**Seção do diário:** *Byte Pair Encoding (BPE): quebrando palavras em partes*  

Mostra como tokenizers modernos lidam com palavras desconhecidas
quebrando-as em subwords ou caracteres.

---

### 06 — Janela deslizante e pares input–target
**Arquivo:** `06-sliding-window.png`  
**Seção do diário:** *Janela deslizante: como o modelo aprende de fato*  

Ilustra como o treinamento de LLMs é feito usando janelas deslocadas
e máscara causal.

---

### 07 — Pipeline completo de entrada do GPT
**Arquivo:** `07-gpt-input-pipeline.png`  
**Seção do diário:** *O pipeline completo de entrada de um GPT-like*  

Mostra o caminho completo desde o texto bruto até os embeddings
que entram no modelo GPT-like.

---

## 🎨 Diretrizes visuais

Todos os infográficos devem:
- manter consistência visual entre si
- usar cores suaves e profissionais
- evitar excesso de texto
- priorizar leitura rápida em artigos técnicos (Medium / Dev.to)

Os prompts detalhados para geração de cada infográfico estão documentados
separadamente e devem ser usados como referência única de criação.
