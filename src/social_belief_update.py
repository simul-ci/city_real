SOCIAL_BELIEF_UPDATE_PROMPT = """You are a social-belief update module for a human-like agent. The agent just had an interaction with a contact. Update the agent's subjective beliefs about this contact based on how the interaction went.

Agent persona: {persona}
Contact: {friend_name} (prior relationship {relationship_score}/100)
Modality: {mode}                      # 'online' or 'offline'
Interaction summary: {interaction_summary}
Outcome / agent's reaction: {interaction_outcome}     # e.g., positive, neutral, negative

Prior beliefs about this contact (each in [0,1]):
- affinity:    {affinity}
- trust:       {trust}
- familiarity: {familiarity}

Rules
- Update each belief in [0,1], higher = stronger; only move a belief if the interaction materially affected it (|Δ| ≥ 0.05).
- Familiarity tends to rise with any interaction; affinity and trust move with the outcome's valence.
- Keep changes gradual; a single interaction should not swing a belief drastically.
- These beliefs shape later decisions such as whom to contact, whether to eat alone, or whether to join a group activity.

Output (JSON only; no extra text), round to 3 decimals:
{
  "affinity": <float 0..1>,
  "trust": <float 0..1>,
  "familiarity": <float 0..1>,
  "reason": "<≤20 words>"
}
"""
