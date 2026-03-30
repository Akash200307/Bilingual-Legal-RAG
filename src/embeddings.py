from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def get_minilm_embed():
    return HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_bge_small_embed():
    return HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

def get_bge_base_embed():
    return HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")