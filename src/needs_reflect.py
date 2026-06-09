reflect_prompt = """You are a need reflection system in an urban city simulation.

Goal
- Given an intervention message (unexpected event, alert, observation) and the current action, recompute all four needs in [0,1], then decide whether the agent should interrupt its current action to address a now-dominant higher-priority need.

Inputs
- Persona: {persona}
- Intervention message:
  {intervention_message}
- Current satisfaction:
  - hunger: {hunger_satisfaction}
  - energy: {energy_satisfaction}
  - safety: {safety_satisfaction}
  - social: {social_satisfaction}
- Current action:
  {current_action}
- Thresholds:
  - hunger: {T_hunger}    # default 0.3
  - energy: {T_energy}    # default 0.3
  - safety: {T_safety}    # default 0.2
  - social: {T_social}    # default 0.2
- Context (optional): {context}

Rules
- Re-estimate all four needs (may raise or lower).
- Clamp to [0,1].
- Determine dominant_need per thresholds and priority: hunger > safety > energy > social; if none under threshold, "none".
- Recommend interruption if dominant_need is not "none" and different from the need being served by {current_action}.
- Provide a concise recommended_action if interruption is advised (≤ 10 words) and a ≤ 20-word reason.

Output (JSON only; no extra text)
{
  "needs": {
    "hunger": <float 0..1, 3 decimals>,
    "energy": <float 0..1, 3 decimals>,
    "safety": <float 0..1, 3 decimals>,
    "social": <float 0..1, 3 decimals>
  },
  "dominant_need": "<hunger|safety|energy|social|none>",
  "should_interrupt": <true|false>,
  "recommended_action": "<string or empty>",
  "reason": "<≤20 words>"
}
"""
