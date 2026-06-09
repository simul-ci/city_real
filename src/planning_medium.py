medium_activity_prompt = """You are refining the agent's schedule by filling MEDIUM-priority essentials (meals, hygiene, childcare, important errands).

Agent attributes:
- Age: {age}
- Gender: {gender}
- Occupation: {occupation}
- Life Stage: {life_stage}
- Health Status: {health_status}
- Fatigue: {fatigue}
- Household Composition: {household_composition}
- Current Day of Week: {day_of_week}

Context:
{context}

Current skeleton (JSON):
{partial_plan_json}

Instructions:
1) Fill ONLY blocks labeled "EMPTY" ("importance":"unfilled") with MEDIUM-priority tasks.
2) You MAY split an EMPTY block into smaller blocks; ensure **5-minute alignment**.
3) Some sub-blocks may remain "EMPTY" (unfilled); these flexible windows are resolved at execution time by the intention module, not here.
4) Do NOT modify existing mandatory blocks.
5) Keep schedule sequential, non-overlapping, and time-aligned.
6) Do NOT select specific locations or vehicles here (mobility is handled elsewhere).
7) Set "importance":"medium" on newly created medium-priority tasks.
8) Use realistic timing (e.g., breakfast 06:00–09:00, lunch 11:30–13:30, dinner 18:00–20:30), adapted to persona/habits/needs.

Each filled block must include:
- "start": "HH:MM" (5-min aligned)
- "end": "HH:MM"   (5-min aligned)
- "activity": e.g., "Shower", "Prepare and eat lunch", "Grocery errand"
- "importance": "medium"
- "source": e.g., "habit", "persona", "needs", "household"
- "reason": short explanation

Return the entire updated schedule as:
{
  "schedule": [ ... all blocks including unchanged mandatory, updated empties ... ]
}
No extra text.
"""
