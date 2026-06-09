place_type_prompt = """Refine a chosen POI TYPE to a more specific subtype.

Inputs
- Primary place type: {primary_place_type}
- User Plan: {plan}
- Persona: {persona}
- Intention: {intention}
- Other information:
-------------------------
{other_info}
-------------------------
- Context (optional): {context}

Allowed subtypes: {poi_category}

Rules
- Return exactly one subtype from {poi_category} that is a valid refinement of {primary_place_type}.
- Prefer options feasible under time/weather, persona, and financial constraints.

Output (JSON only; no extra text)
{
  "place_type": "<one of poi_category>",
  "reason": "<≤15 words>"
}
"""
