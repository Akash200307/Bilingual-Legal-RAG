from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex,StorageContext,Settings
from src.llm_model import Groq_model
import chromadb



llm=Groq_model()
def build_chroma_index(nodes,persis_dir,collection_name:str,embed_model):
    chroma_client=chromadb.PersistentClient(path=persis_dir)
    collection=chroma_client.get_or_create_collection(collection_name)
    vector_store=ChromaVectorStore(collection)
    storage_ctx=StorageContext.from_defaults(vector_store=vector_store)
    Settings.embed_model=embed_model
    Settings.llm=llm
    index=VectorStoreIndex(nodes,storage_context=storage_ctx)
    print("Index creation started")
    return index


def load_index(embed_model, persistent_dir: str, collection_name: str):
    chroma_client = chromadb.PersistentClient(path=persistent_dir)
    chroma_collection =chroma_client.get_or_create_collection(collection_name)
    Settings.embed_model=embed_model
    Settings.llm=llm
    vector_store=ChromaVectorStore(chroma_collection)
    storage_ctx=StorageContext.from_defaults(vector_store=vector_store)
    return VectorStoreIndex.from_vector_store(vector_store=vector_store,storage_context=storage_ctx)


