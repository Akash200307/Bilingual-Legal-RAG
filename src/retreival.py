def make_query_engine(index,top_n=5):
    return index.as_query_engine(similarity_top_k=top_n)