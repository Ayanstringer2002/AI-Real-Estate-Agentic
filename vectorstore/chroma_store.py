import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection(name="properties")

def add_documents(ids, documents, embeddings):
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )

def query_collection(query_embedding, n_results=5):
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )