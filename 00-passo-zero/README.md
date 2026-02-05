# Passo Zero — Ambiente, Colab, PyTorch e Fundamentos

Este é o capítulo que prepara o terreno para a série **Fazendo um LLM do Zero**.

Aqui você vai aprender:
- o que é o Google Colab e por que ele é ideal para acompanhar a série
- como usar o Colab (do clique ao “Run all”)
- o que é o PyTorch e qual o papel dele na construção de LLMs
- o que são bibliotecas em Python (pip, imports, dependências)
- como garantir reprodutibilidade mínima (seeds, versões, device)

---

## ▶️ Comece por aqui

1) Leia o diário (origem do post no Medium):
- `diario.md`

2) Rode o notebook:
- `notebook.ipynb`

3) Use os links diretos:
- `links.md`

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

