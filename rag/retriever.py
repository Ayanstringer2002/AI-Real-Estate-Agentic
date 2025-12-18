from embeddings.embedder import embed_texts
from vectorstore.chroma_store import query_collection


def retrieve_context(query):
    query_embedding = embed_texts([query])[0]
    results = query_collection(query_embedding)
    return results["documents"][0]