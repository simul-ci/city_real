area_selection_prompt = """You are an area selector in an urban simulation. Decide whether to stay nearby or travel further by choosing ONE area from the candidate list, given the agent's active intention.

Inputs
- User Plan: {plan}
- Persona: {persona}
- Intention: {intention}
- Beliefs about places/areas: {beliefs}
- Social context: {social_context}
- Financial pressure (0-1, higher = more constrained): {financial_pressure}
- Candidate Areas (JSON array): {candidate_areas}
- Context: {context}

Rules
- Prefer areas that fit the intention AND the time budget (short budget → nearer areas).
- If energy is low, bad weather, or safety concerns, favor closer/indoor-friendly areas.
- If financial pressure is high, favor nearer, lower-cost areas and avoid long, expensive trips.
- If leisure window is large and emotion positive, longer trips are acceptable.
- An intention to run errands may target an area with multiple relevant POIs; an intention to relax may prefer a specific park or cafe.

Output (JSON only; no extra text)
{
  "area_id": "<from candidate_areas>",
  "area_name": "<string>",
  "reason": "<≤20 words>"
}
"""
