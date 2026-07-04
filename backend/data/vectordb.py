# backend/data/vectordb.py
import chromadb
from sentence_transformers import SentenceTransformer
from data.memory_data import DATA

# 1. Load the embedding model (runs locally, no API cost)
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Create an in-memory Chroma DB
client = chromadb.Client()
collection = client.get_or_create_collection(name="business_memory")

# 3. Add our 12 synthetic cases to the DB
for item in DATA:
    text_to_embed = f"Decision: {item['decision']}. Outcome: {item['outcome']}. Reason: {item['reason']}"
    embedding = model.encode(text_to_embed).tolist()
    
    collection.add(
        ids=[str(item['id'])],
        embeddings=[embedding],
        metadatas=[{"text": text_to_embed, "outcome": item['outcome']}]
    )

def retrieve_memory(query_text, top_k=1):
    """
    Queries the vector DB and returns the best matching memory 
    along with the REAL Cosine Similarity score (0 to 1).
    """
    query_embedding = model.encode(query_text).tolist()
    results = collection.query(
        query_embeddings=[query_embedding], 
        n_results=top_k,
        include=["metadatas", "distances"]  # Request distances to calculate similarity
    )
    
    if results['metadatas'] and len(results['metadatas'][0]) > 0:
        # ChromaDB returns 'distance'. Cosine Similarity = 1 - distance.
        raw_distance = results['distances'][0][0]
        similarity_score = round(1 - raw_distance, 4)  # e.g., 0.8845
        
        best_text = results['metadatas'][0][0]['text']
        return best_text, similarity_score
    
    return "No relevant past memory found.", 0.0