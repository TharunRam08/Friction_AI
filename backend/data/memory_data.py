# backend/data/memory_data.py
import json

DATA = [
    {
        "id": 1, 
        "decision": "Expanded to second location in 2024", 
        "outcome": "Failed", 
        "reason": "Logistics capacity insufficient; warehouse at 92% utilization. Could not handle cross-city inventory transfer.",
        "impact": "negative"
    },
    {
        "id": 2, 
        "decision": "Hired 10 sales reps in Q1 2025", 
        "outcome": "Success", 
        "reason": "Demand was high, sales pipeline cleared within 2 months. Revenue increased by 18%.",
        "impact": "positive"
    },
    {
        "id": 3, 
        "decision": "Cut prices by 10% to compete with new market entrant", 
        "outcome": "Mixed", 
        "reason": "Increased volume by 25% but destroyed gross margins by 12%. Profit remained flat.",
        "impact": "neutral"
    },
    {
        "id": 4, 
        "decision": "Invested in warehouse automation software", 
        "outcome": "Success", 
        "reason": "Reduced operational overhead by 15% and picking errors dropped to near zero.",
        "impact": "positive"
    },
    {
        "id": 5,
        "decision": "Outsourced logistics to a third-party provider",
        "outcome": "Failed",
        "reason": "Third-party provider failed to meet SLAs. Customer complaints about late deliveries increased by 40%.",
        "impact": "negative"
    },
    {
        "id": 6,
        "decision": "Launched a new premium product line",
        "outcome": "Success",
        "reason": "Differentiated the brand. High margins offset the lower volume. Customer acquisition cost decreased.",
        "impact": "positive"
    },
    {
        "id": 7,
        "decision": "Increased marketing spend on social media by 50%",
        "outcome": "Mixed",
        "reason": "Brand awareness increased significantly, but conversion rate was low. Cost per acquisition was too high.",
        "impact": "neutral"
    },
    {
        "id": 8,
        "decision": "Expanded operations to a new city (2023)",
        "outcome": "Failed",
        "reason": "Underestimated local competition. Did not localize the product offering. Exited market after 6 months.",
        "impact": "negative"
    },
    {
        "id": 9,
        "decision": "Implemented a customer referral program",
        "outcome": "Success",
        "reason": "Loyal customers brought in high-quality leads. Customer lifetime value increased by 22%.",
        "impact": "positive"
    },
    {
        "id": 10,
        "decision": "Hired a full-time Chief Technology Officer",
        "outcome": "Success",
        "reason": "Tech debt was reduced. Product development velocity increased by 30%.",
        "impact": "positive"
    },
    {
        "id": 11,
        "decision": "Moved to a remote-first work policy",
        "outcome": "Mixed",
        "reason": "Employee satisfaction increased, but collaboration and innovation metrics slightly declined.",
        "impact": "neutral"
    },
    {
        "id": 12,
        "decision": "Secured a large inventory purchase at a discount",
        "outcome": "Failed",
        "reason": "Warehouse had no space for the extra inventory. Had to rent expensive external storage, eating the discount.",
        "impact": "negative"
    }
]
MEMORY_STRING = json.dumps(DATA, indent=2)