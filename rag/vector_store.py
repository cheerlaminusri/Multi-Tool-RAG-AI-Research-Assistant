import faiss
import numpy as np

class VectorStore:
    
    def __init__(self, dim):
        # Initialize FAISS index using L2 (Euclidean) distance
        self.index = faiss.IndexFlatL2(dim)  # dim = embedding dimension (example: 384 for all-MiniLM-L6-v2)
        
        # List to store original documents corresponding to embeddings
        self.docs = []

    def add(self, embeddings, docs):
        # Convert embeddings to numpy array and ensure float32 type
        # FAISS requires embeddings in float32 format
        embeddings = np.array(embeddings).astype("float32")
        
        # Add embeddings to the FAISS index
        self.index.add(embeddings)
        
        # Store corresponding documents in the docs list
        self.docs.extend(docs)

    def search(self, query_embedding, k=20):
        # Convert query embedding to numpy float32
        # reshape(1, -1) ensures FAISS receives a 2D array
        query_embedding = np.array(query_embedding).astype("float32").reshape(1, -1)
        
        # Perform similarity search
        # D = distances of nearest vectors
        # I = indices of nearest vectors in the index
        D, I = self.index.search(query_embedding, k)
        
        # Retrieve documents using returned indices
        # Ignore invalid indices (-1)
        results = [self.docs[i] for i in I[0] if i != -1]
        
        # Return top-k similar documents
        return results