BELIEF_ESTIMATE_PROMPT = """You are a belief initialization system for a human-like agent. The agent has never visited {place_name} before.

Agent Profile:
- Gender: {gender}
- Education Level: {education}
- Consumption Level: {consumption}
- Occupation: {occupation}
- Age: {age}
- Monthly Income: {income}

Similar places previously visited by the agent (may include names, categories, and/or belief vectors):
{similar_places}

Estimate the agent's beliefs about {place_name} on four dimensions in [0,1], where higher is better:
- affordability  (price satisfaction / value; higher = cheaper/better value than expected)
- convenience    (ease of access and use)
- crowding       (higher = more comfortable / less crowded than expected)
- enjoyment      (overall satisfaction with the experience)

If specific belief vectors for similar places are provided, use them to inform your estimate; otherwise infer from categories and profile. If information is insufficient, return neutral 0.500 values.

Respond in JSON only (no extra text), round to 3 decimals, e.g.:
{
  "affordability": 0.600,
  "convenience": 0.400,
  "crowding": 0.700,
  "enjoyment": 0.750
}
"""
