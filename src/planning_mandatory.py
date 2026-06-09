high_priority_prompt = """As an intelligent agent's plan system, create a DAILY SKELETON that ONLY includes MANDATORY activities:
- Sleep (must be included)
- Work or school (if relevant to the agent's occupation)
- Commute segments to/from work/school when location ≠ home
- Medical appointments or other unavoidable obligations (if any)
- Recurring household obligations inferred for this agent (if any)

All other time periods must be explicitly filled with a placeholder labeled "EMPTY".

Schedule requirements:
- Cover 00:00 to 24:00 inclusive
- Sequential, non-overlapping blocks
- Variable durations
- **All start/end times aligned to 5-minute increments**

Agent attributes:
- Age: {age}
- Gender: {gender}
- Occupation: {occupation}
- Life Stage: {life_stage}
- Health Status: {health_status}
- Fatigue: {fatigue}
- Household Composition: {household_composition}
- Current Day of Week: {day_of_week}

Optional context: {context}
# MAY include:
# {"home_location":"...", "work_location":"...", "is_remote":false,
#  "known_commitments":[{"start":"14:30","end":"15:15","activity":"Doctor"}],
#  "recurring_obligations":[{"name":"School pickup","frequency":"workdays"}],
#  "typical_work_hours":"09:00-17:30"}

Response format:
Return a JSON object with a single key "schedule" whose value is an array of blocks.
Each block must contain:
- "start": "HH:MM" (5-min aligned)
- "end":   "HH:MM" (5-min aligned)
- "activity": e.g., "Sleep", "Work", "Commute to work", or "EMPTY"
- "importance": "mandatory" or "unfilled"
- "source": e.g., "sleep_need", "occupation", "appointment", "obligation"
- "reason": short explanation

Do not include any extra text. Example shape only:

{
  "schedule": [
    {
      "start": "00:00",
      "end": "06:30",
      "activity": "Sleep",
      "importance": "mandatory",
      "source": "sleep_need",
      "reason": "Overnight rest based on fatigue and routine"
    },
    {
      "start": "06:30",
      "end": "08:00",
      "activity": "EMPTY",
      "importance": "unfilled",
      "source": "",
      "reason": ""
    },
    {
      "start": "08:00",
      "end": "08:45",
      "activity": "Commute to work",
      "importance": "mandatory",
      "source": "occupation",
      "reason": "Travel from home to workplace"
    },
    ...
  ]
}"""
