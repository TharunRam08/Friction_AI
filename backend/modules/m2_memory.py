# backend/modules/m2_memory.py
from data.vectordb import retrieve_memory

def get_past_context(question: str, goal: str) -> tuple:
    """
    Returns: (past_memory_text, actual_cosine_similarity_score)
    """
    search_query = f"{question} {goal}"
    past_memory, similarity_score = retrieve_memory(search_query)
    return past_memory, similarity_score
