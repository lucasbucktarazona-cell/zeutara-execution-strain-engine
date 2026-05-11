import json

def analyze_company(data):
    founder_post = data.get("founder_post", "").lower()
    employee_growth = data.get("employee_growth", "").lower()
    open_roles = data.get("open_roles", [])

    score = 5

    if "scale" in founder_post or "scaling" in founder_post:
        score += 1.5
    if "coordination" in founder_post or "prioritization" in founder_post:
        score += 1.5
    if "revops" in str(open_roles).lower() or "growth" in str(open_roles).lower():
        score += 1
    if "to" in employee_growth:
        score += 1

    score = min(score, 10)

    if score >= 8:
        priority = "High"
    elif score >= 6:
        priority = "Medium"
    else:
        priority = "Low"

    return {
        "company": data.get("company"),
        "execution_strain_score": score,
        "priority_level": priority,
        "likely_bottleneck": "GTM coordination, prioritization, and operational scaling",
        "recommended_zeutara_angle": "Execution architecture to help the founder convert growth into repeatable systems",
        "outbound_draft": f"Saw that {data.get('company')} has been scaling quickly. Given the recent growth and operational complexity, there may be an opportunity to tighten execution architecture around GTM, prioritization, and internal coordination.",
        "reasoning_summary": "The company shows signals of execution strain through growth, scaling language, and roles related to GTM or operations."
    }
