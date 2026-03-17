from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    # Convert text(s) to vector embeddings
    return model.encode(texts)