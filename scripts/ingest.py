from data.loader import load_properties
from embeddings.embedder import embed_texts
from vectorstore.chroma_store import add_documents


def ingest():
    df = load_properties()
    embeddings = embed_texts(df["content"].tolist())
    add_documents(
        ids=df["id"].astype(str).tolist(),
        documents=df["content"].tolist(),
        embeddings=embeddings
    )

if __name__ == "__main__":
    ingest()