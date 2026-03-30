from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.postprocessor.flag_embedding_reranker import  FlagEmbeddingReranker

def get_cross_encoder_reranker(top_n=6):
    """Lightweight MS-MARCO cross-encoder — fast on CPU"""
    return SentenceTransformerRerank(
        model="cross-encoder/ms-marco-MiniLM-L-6-v2",
        top_n=top_n
    )

def get_bge_reranker(top_n=6):
    """BGE reranker — better quality, ~2x slower"""
    return FlagEmbeddingReranker(
        model="BAAI/bge-reranker-v2-m3",
        top_n=top_n
    )