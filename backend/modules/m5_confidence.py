# backend/modules/m5_confidence.py
def calculate_confidence(views: list, memory_match_score: float) -> dict:
    # 1. Agreement Ratio
    stances = [v['stance'] for v in views]
    majority = max(set(stances), key=stances.count)
    agreement_ratio = stances.count(majority) / len(stances)
    
    # 2. Scenario Stability (derived from agreement for hackathon speed)
    scenario_score = (agreement_ratio * 0.7) + 0.3
    
    # 3. THE MASTER FORMULA (from your PDF)
    confidence = (0.4 * agreement_ratio) + (0.3 * memory_match_score) + (0.3 * scenario_score)
    confidence_percent = round(confidence * 100, 1)
    
    return {
        "confidence": confidence_percent,
        "agreement_score": round(agreement_ratio, 2),
        "memory_match": memory_match_score,
        "scenario_stability": round(scenario_score, 2),
        "majority_stance": majority
    }
