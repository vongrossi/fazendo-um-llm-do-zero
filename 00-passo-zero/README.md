# Passo Zero — Ambiente, Colab, PyTorch e Fundamentos

Este é o capítulo que prepara o terreno para a série **Fazendo um LLM do Zero**.

Aqui você vai aprender:
- o que é o Google Colab e por que ele é ideal para acompanhar a série
- como usar o Colab (do clique ao “Run all”)
- o que é o PyTorch e qual o papel dele na construção de LLMs
- o que são bibliotecas em Python (pip, imports, dependências)
- como garantir reprodutibilidade mínima (seeds, versões, device)

---

## 📊 Infográficos

Este capítulo utiliza infográficos para reforçar visualmente conceitos como:

- o ambiente Google Colab
- o papel do PyTorch
- o funcionamento de bibliotecas Python

As descrições dos infográficos estão documentadas em:

- `infograficos/README.md`

---

## ▶️ Como executar

1. Leia o diário do capítulo:
   - `diario.md`

2. Execute o notebook:
   - `notebook.ipynb`

3. Ou abra diretamente no Google Colab:
   - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vongrossi/fazendo-um-llm-do-zero/blob/main/00-passo-zero/notebook.ipynb)
   - ou veja mais detalhes em `links.md`

---

## 📌 Nota sobre dependências

Este capítulo foi pensado para rodar **no Colab padrão**.
Mesmo assim, incluímos um `requirements.txt` para:
- documentar dependências
- permitir execução local (opcional)
- manter consistência ao longo da série

No Colab, você *pode* instalar com:

```bash
!pip -q install -r requirements.txt
```

