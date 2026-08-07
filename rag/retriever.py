import chromadb
from sentence_transformers import SentenceTransformer

DB_PATH="./data/vector_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_knowledge(query, top_k=5):
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection("knowledge_base")
    
    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
    )

    findings = []

    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        findings.append({
            "source": meta.get("source"),
            "content": doc,
        })

    return findings