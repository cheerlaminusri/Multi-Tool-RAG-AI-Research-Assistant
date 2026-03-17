from sentence_transformers import CrossEncoder

# Load cross-encoder model for reranking
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs):
    
    # Create (query, document) pairs
    pairs = [(query, d.page_content) for d in docs]

    # Predict relevance scores
    scores = reranker.predict(pairs)

    # Sort documents by score (highest first)
    ranked = sorted(zip(scores, docs),key=lambda x: x[0],reverse=True)

    # Return top 5 reranked documents
    return [doc for _, doc in ranked[:5]]