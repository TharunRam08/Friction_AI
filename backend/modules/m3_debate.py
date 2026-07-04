# backend/modules/m3_debate.py
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

def debate_persona(question: str, goal: str, history: str, persona: str, bias: str, model) -> dict:
    prompt = f"""
    You are the {persona} Director. {bias}
    The company is considering: "{question}".
    The strategic goal is: {goal}.
    Historical context from our company records: {history}.

    Based ONLY on your department's perspective, give your stance: "Support", "Neutral", or "Against".
    Provide 2 strong reasons.
    Return ONLY a JSON object with keys: "stance", "reasons" (list of strings).
    """
    response = model.generate_content(prompt)
    clean_json = response.text.replace('```json', '').replace('```', '').strip()
    return json.loads(clean_json)

def run_debate(question: str, goal: str, past_memory: str, model) -> list:
    personas = [
        {"name": "Finance", "bias": "You prioritize cash preservation. You are highly conservative and hate risk."},
        {"name": "Operations", "bias": "You obsess over logistics, warehouse capacity, and current workloads. You hate bottlenecks."},
        {"name": "Sales", "bias": "You are aggressively optimistic. You believe any lost customer is permanent and push for growth at all costs."},
        {"name": "HR", "bias": "You focus on recruitment pipeline health and company culture. You hate rapid, unplanned hiring."}
    ]
    
    views = [None] * 4
    with ThreadPoolExecutor(max_workers=4) as executor:
        future_map = {}
        for i, p in enumerate(personas):
            future = executor.submit(debate_persona, question, goal, past_memory, p['name'], p['bias'], model)
            future_map[future] = i
        
        for future in as_completed(future_map):
            idx = future_map[future]
            views[idx] = future.result()
    
    return views
