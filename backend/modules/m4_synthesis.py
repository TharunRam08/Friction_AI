# backend/modules/m4_synthesis.py
import json

def synthesize(question: str, goal: str, views: list, model) -> str:
    views_text = json.dumps(views, indent=2)
    prompt = f"""
    You are the CEO. Your goal is: {goal}. 
    You asked: {question}.
    Your 4 department heads gave these exact independent opinions:
    {views_text}

    Reconcile these conflicting views. Identify the single biggest constraint (the binding factor).
    Produce a final, actionable, conditional recommendation (e.g., "Delay expansion, fix logistics first, then proceed").
    """
    response = model.generate_content(prompt)
    return response.text.strip()
