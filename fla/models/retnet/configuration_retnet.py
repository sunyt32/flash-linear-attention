# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Optional

from transformers.configuration_utils import PretrainedConfig


class RetNetConfig(PretrainedConfig):

    model_type = 'retnet'
    keys_to_ignore_at_inference = ['past_key_values']

    def __init__(
        self,
        vocab_size: int = 32000,
        hidden_size: int = 2048,
        expand_k: int = 0.5,
        expand_v: int = 1,
        intermediate_size: Optional[int] = None,
        num_hidden_layers: int = 24,
        num_attention_heads: int = 8,
        num_key_value_heads: Optional[int] = None,
        attn_mode: str = "fused_chunk",
        hidden_act: str = "swish",
        max_position_embeddings: int = 2048,
        rms_norm_eps: float = 1e-6,
        use_gk: bool = True,
        use_gv: bool = False,
        use_cache: bool = True,
        pad_token_id: int = None,
        bos_token_id: int = 0,
        eos_token_id: int = 0,
        tie_word_embeddings: bool = False,
        fuse_norm: bool = True,
        fuse_cross_entropy: bool = True,
        **kwargs
    ) -> RetNetConfig:
        self.vocab_size = vocab_size
        self.max_position_embeddings = max_position_embeddings
        self.hidden_size = hidden_size
        self.expand_k = expand_k
        self.expand_v = expand_v
        self.intermediate_size = intermediate_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads

        # for backward compatibility
        if num_key_value_heads is None:
            num_key_value_heads = num_attention_heads

        self.num_key_value_heads = num_key_value_heads
        self.attn_mode = attn_mode
        self.hidden_act = hidden_act
        self.rms_norm_eps = rms_norm_eps
        self.use_gk = use_gk
        self.use_gv = use_gv
        self.use_cache = use_cache
        self.fuse_norm = fuse_norm
        self.fuse_cross_entropy = fuse_cross_entropy

        super().__init__(
            pad_token_id=pad_token_id,
            bos_token_id=bos_token_id,
            eos_token_id=eos_token_id,
            tie_word_embeddings=tie_word_embeddings,
            **kwargs,
        )