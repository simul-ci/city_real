init_prompt = """You are a need initialization system in an urban city simulation.

Goal
- Initialize the four core need satisfactions in [0,1], propose decay rates α_n, set thresholds T_n (use defaults if unspecified), and compute the current dominant_need following the fixed priority: hunger > safety > energy > social.

Inputs
- Profile:
  {persona}
  - Monthly Income (net): {income}
- Current Time: {now_time}
- Financial pressure (0-1, higher = more constrained): {financial_pressure}
- Context: {context}

Rules
- Satisfaction values are floats in [0,1], where lower = less satisfied / more pressing.
- Financial security is modeled separately as a continuous financial-pressure signal (see below); when financial pressure is high, safety_satisfaction should tend to be lower.
- Typical rhythms:
  - hunger_satisfaction tends to be lower at usual mealtimes.
  - energy_satisfaction tends to be lower overnight/late-night if sleep debt exists.
- Provide decay_rates α_n per need (reasonable small positive values; these will be applied per 5-minute tick in code).
- Use thresholds T_n = { hunger: 0.3, energy: 0.3, safety: 0.2, social: 0.2 } unless {context} specifies overrides.
- Compute dominant_need as the highest-priority need whose satisfaction ≤ its threshold; if none under threshold, set dominant_need = "none".

Output (JSON only; no extra text)
{
  "current_satisfaction": {
    "hunger": <float 0..1, 3 decimals>,
    "energy": <float 0..1, 3 decimals>,
    "safety": <float 0..1, 3 decimals>,
    "social": <float 0..1, 3 decimals>
  },
  "decay_rates": {
    "hunger": <float >0>,
    "energy": <float >0>,
    "safety": <float >0>,
    "social": <float >0>
  },
  "thresholds": {
    "hunger": 0.3,
    "energy": 0.3,
    "safety": 0.2,
    "social": 0.2
  },
  "dominant_need": "<hunger|safety|energy|social|none>"
}
"""
