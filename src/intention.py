intention_formation_prompt = """You are simulating a realistic person deciding what to do during a flexible block of free time.
Form a single coherent INTENTION: a compact natural-language description of what this person is trying to accomplish now, which provides shared context for the next several decisions instead of choosing each step independently.

CURRENT STATE:
- Time: {current_time}, {day_of_week}
- Weather: {weather}
- Location: {location_context}
- Free time available: {free_duration_min} minutes
- Next commitment: {next_commitment_context}

ABOUT THIS PERSON:
{persona_summary}
Household: {household_summary}

PHYSICAL / INTERNAL STATE (0-1, 1 = satisfied):
- Hunger: {hunger_satisfaction}
- Energy: {energy_satisfaction}
- Social: {social_satisfaction}
- Current mood: {emotion_types}

ECONOMIC STATE:
- Financial pressure (0-1, higher = more constrained): {financial_pressure}

HABITS AND MEMORY:
- Recent patterns / habits: {recent_patterns}
- Reflective insights: {reflective_insights}
- Recurring obligations: {obligations_context}
- Intentions already pursued today: {today_intentions}

NEARBY / AVAILABLE AREAS:
{area_options}

Soft behavioral tendencies for this person:
{behavioral_adapter}

Rules
- Produce ONE intention that can plausibly fill the available time and respects the next commitment.
- Decide whether to go out or stay home given energy, weather, mood, needs, and financial pressure (high pressure biases toward cheaper or stay-home options).
- The intention is a goal, not a fixed itinerary: it may span multiple nearby places (e.g., run errands near the station).
- If going out, optionally anchor the intention to ONE area from the list.
- Keep the intention compact and specific (e.g., "find an inexpensive meal before returning home").

Output (JSON only; no extra text)
{
  "reasoning": "<brief explanation>",
  "decision": "go_out" | "stay_home",
  "intention": "<compact natural-language goal>",
  "area_anchor": "<area name from the list, or empty if staying home / local>",
  "expected_duration_min": <integer minutes, multiple of 5>,
  "status": "active"
}
"""
