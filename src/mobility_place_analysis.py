place_analysis_prompt = """Analyze the intention and produce POI FILTERS/CONSTRAINTS for micro-level selection (a belief-aware gravity model will rank candidates).

Inputs
- User Plan: {plan}
- Persona: {persona}
- Intention: {intention}
- Financial pressure (0-1): {financial_pressure}
- Other information:
-------------------------
{other_info}
-------------------------
- Context (optional): {context}

Allowed canonical places (optional): {place_list}
  # If the intention clearly maps to one canonical class (e.g., "home","work"),
  # you MAY set "canonical_place" to one of these. Otherwise omit it.

Rules
- Do NOT choose a specific POI; your output feeds a gravity scorer.
- Provide only constraints/filters; keep them realistic and consistent with persona, intention, and financial pressure (high pressure → lower price_tier).

Output (JSON only; no extra text)
{
  "canonical_place": "<one of place_list or empty>",
  "filters": {
    "poi_types": ["<one or more types>"],
    "indoor": <true|false|null>,
    "price_tier": "<low|mid|high|null>",
    "quietness": "<low|medium|high|null>",
    "kid_friendly": <true|false|null>,
    "accessibility_required": <true|false|null>,
    "max_radius_m": <integer or null>,
    "time_budget_min": <integer or null>
  }
}
"""
