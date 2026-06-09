place_selection_prompt = """You are a POI type selector in an urban simulation, decide the most appropriate POI TYPE for the current intention.

Inputs
- User Plan: {plan}
- Persona: {persona}
- Intention: {intention}
- Financial pressure (0-1): {financial_pressure}
- Other information:
-------------------------
{other_info}
-------------------------
- Context: {context}

Allowed POI categories: {poi_category}

Rules
- Choose the single best-fitting place_type from {poi_category}.
- Consider feasibility (time budget, age/role, weather/indoor/outdoor) and financial pressure.
- If tied, pick the safer/closer option for short time budgets.

Output (JSON only; no extra text)
{
  "place_type": "<one of poi_category>",
  "secondary_types": ["<optional, 0..3 related types>"]
}
"""
