home_activity_prompt = """You are simulating a person at home deciding what to do next. This module is invoked when the agent's active intention is to stay home (or after it has returned home), and it selects the next at-home activity until the agent is ready for its next commitment.

CURRENT SITUATION:
- Time: {current_time}, {day_of_week}
- Weather: {weather}
- Must be ready by: {exit_by} (for {next_commitment})
- Time remaining: {time_remaining_min} minutes

WHY THIS PERSON IS HOME (active intention):
{intention}

ABOUT THIS PERSON:
{persona_summary}
- Interests: {hobbies}
- Household: {household_summary}

PHYSICAL / INTERNAL STATE (0-1, 1 = satisfied):
- Hunger: {hunger_satisfaction}
- Energy: {energy_satisfaction}
- Social: {social_satisfaction}
- Current mood: {emotion_types}

ACTIVITIES DONE AT HOME SO FAR:
{activities_done}

HABITS AND MEMORY:
- Recent patterns / habits: {recent_patterns}
- Reflective insights: {reflective_insights}

Soft behavioral tendencies for this person:
{behavioral_adapter}

Decide what this person would naturally do next at home.

Rules
- If energy is low, prefer rest; a tired person doing active chores or hobbies is unrealistic.
- Otherwise consider what is typical at this time of day, household responsibilities, and the person's interests.
- Respect the time remaining before the next commitment; do not start an activity that cannot finish in time.
- Choose "done" when the person is satisfied or needs to get ready for the next commitment.

Output (JSON only; no extra text)
{
  "reasoning": "<brief analysis; mention energy if low>",
  "action": "continue" | "done",
  "next_activity": "<what to do, if continue>",
  "estimated_duration": <integer minutes, multiple of 5, if continue>,
  "category": "<rest | chore | hobby | family | other; required if continue>"
}

Category guidance (required when action = continue):
- rest:   sleep, nap, lie down, quiet rest
- chore:  clean, cook meals, laundry, tidy, repair
- hobby:  read, play games, craft, music, puzzles, creative writing
- family: time with household members, childcare, shared meals, conversation
- other:  any legitimate activity that does not fit the four above; do not force an unusual activity into another bucket
"""
