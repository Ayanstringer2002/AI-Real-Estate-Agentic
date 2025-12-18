from fastembed import TextEmbedding

embedder = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

def embed_texts(texts):
    return list(embedder.embed(texts))