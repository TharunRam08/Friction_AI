# backend/modules/m1_intent.py
import json

def get_intent(question: str, model) -> dict:
    prompt = f"""
    You are a business strategist. Read the user's question: "{question}".
    Extract the underlying business goal, constraints, and time horizon.
    Return ONLY a valid JSON object with these exact keys: "goal", "constraints", "time_horizon".
    Example: {{"goal": "Increase Market Share", "constraints": ["Maintain Margin"], "time_horizon": "3 Months"}}
    """
    response = model.generate_content(prompt)
    clean_json = response.text.replace('```json', '').replace('```', '').strip()
    return json.loads(clean_json)
