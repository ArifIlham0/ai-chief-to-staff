import os
import fitz
import chromadb
from sentence_transformers import SentenceTransformer

DOCS_PATH="./data/docs"
DB_PATH="./data/vector_db"

model = SentenceTransformer("all-MiniLM-L6-v2")

def read_pdf(path):
    doc = fitz.open(path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text

def chunk_text(text, chunk_size=800):
    words = text.split()

    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]

def ingest_documents():
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_or_create_collection("knowledge_base")

    doc_id = 0

    for file in os.listdir(DOCS_PATH):
        path = os.path.join(DOCS_PATH, file)

        if file.endswith(".pdf"):
            text = read_pdf(path)
        elif file.endswith(".txt"):
            text = open(path, "r", encoding="utf-8").read()
        else:
            continue

        chunks = chunk_text(text)

        for chunk in chunks:
            embedding = model.encode(chunk).tolist()

            collection.add(
                ids=[str(doc_id)],
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[{"source": file}]
            )

            doc_id += 1

    print("Documents ingested successfully.")

if __name__ == "__main__":
    ingest_documents()