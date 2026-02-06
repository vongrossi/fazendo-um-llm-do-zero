# lib/gptmini.py
# Núcleo reutilizável do GPTMini (decoder-only Transformer)
# Projeto: Fazendo um LLM do Zero

from dataclasses import dataclass
import math
import torch
import torch.nn as nn
import torch.nn.functional as F


@dataclass
class GPTConfig:
    vocab_size: int
    context_size: int
    d_model: int = 64
    n_heads: int = 4
    n_layers: int = 2
    dropout: float = 0.1


class TokenAndPositionEmbedding(nn.Module):
    def __init__(self, config: GPTConfig):
        super().__init__()
        self.tok_emb = nn.Embedding(config.vocab_size, config.d_model)
        self.pos_emb = nn.Embedding(config.context_size, config.d_model)
        self.dropout = nn.Dropout(config.dropout)

    def forward(self, idx: torch.Tensor) -> torch.Tensor:
        # idx: (B, T)
        B, T = idx.shape
        pos = torch.arange(0, T, device=idx.device).unsqueeze(0)  # (1, T)
        x = self.tok_emb(idx) + self.pos_emb(pos)                 # (B, T, C)
        return self.dropout(x)


class CausalSelfAttention(nn.Module):
    def __init__(self, config: GPTConfig):
        super().__init__()
        assert config.d_model % config.n_heads == 0, "d_model precisa ser divisível por n_heads"
        self.n_heads = config.n_heads
        self.head_dim = config.d_model // config.n_heads
        self.dropout = nn.Dropout(config.dropout)

        self.qkv = nn.Linear(config.d_model, 3 * config.d_model)
        self.out_proj = nn.Linear(config.d_model, config.d_model)

        # máscara causal (T x T) máxima
        self.register_buffer("mask", torch.tril(torch.ones(config.context_size, config.context_size)))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (B, T, C)
        B, T, C = x.shape

        qkv = self.qkv(x)              # (B, T, 3C)
        q, k, v = qkv.split(C, dim=2)

        # (B, nh, T, hs)
        q = q.view(B, T, self.n_heads, self.head_dim).transpose(1, 2)
        k = k.view(B, T, self.n_heads, self.head_dim).transpose(1, 2)
        v = v.view(B, T, self.n_heads, self.head_dim).transpose(1, 2)

        # scores: (B, nh, T, T)
        att = (q @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)

        # aplica máscara causal: bloqueia futuro
        att = att.masked_fill(self.mask[:T, :T] == 0, float("-inf"))

        att = F.softmax(att, dim=-1)
        att = self.dropout(att)

        y = att @ v  # (B, nh, T, hs)

        # volta para (B, T, C)
        y = y.transpose(1, 2).contiguous().view(B, T, C)

        y = self.out_proj(y)
        y = self.dropout(y)
        return y


class FeedForward(nn.Module):
    def __init__(self, config: GPTConfig):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(config.d_model, 4 * config.d_model),
            nn.GELU(),
            nn.Linear(4 * config.d_model, config.d_model),
            nn.Dropout(config.dropout),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class TransformerBlock(nn.Module):
    def __init__(self, config: GPTConfig):
        super().__init__()
        self.ln1 = nn.LayerNorm(config.d_model)
        self.attn = CausalSelfAttention(config)
        self.ln2 = nn.LayerNorm(config.d_model)
        self.ff = FeedForward(config)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Pre-LN (mais estável para treinar)
        x = x + self.attn(self.ln1(x))
        x = x + self.ff(self.ln2(x))
        return x


class GPTMini(nn.Module):
    def __init__(self, config: GPTConfig):
        super().__init__()
        self.config = config
        self.emb = TokenAndPositionEmbedding(config)
        self.blocks = nn.Sequential(*[TransformerBlock(config) for _ in range(config.n_layers)])
        self.ln_f = nn.LayerNorm(config.d_model)
        self.head = nn.Linear(config.d_model, config.vocab_size)

    def forward(self, idx: torch.Tensor, targets: torch.Tensor | None = None):
        # idx: (B, T)
        x = self.emb(idx)              # (B, T, C)
        x = self.blocks(x)             # (B, T, C)
        x = self.ln_f(x)               # (B, T, C)
        logits = self.head(x)          # (B, T, vocab)

        loss = None
        if targets is not None:
            # target esperado: (B,) -> próximo token do contexto
            logits_last = logits[:, -1, :]  # (B, vocab)
            loss = F.cross_entropy(logits_last, targets)

        return logits, loss

