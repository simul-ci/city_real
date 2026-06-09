reflection_prompt = """You are an end-of-day experience-driven reflection module for a human-like agent. Once per day, extract what the agent actually LEARNED from the day's experiences and convert it into reusable behavioral insights. Do not simply summarize the logs: reflect on outcomes by considering what the agent liked or disliked, which constraints shaped its choices, and which habits, preferences, or tendencies emerged.

ABOUT THIS PERSON:
{persona_summary}

DAY SUMMARY:
{day_summary}
# compact summary covering activities, visited places, spending, social interactions, unmet needs, and deviations from the planned schedule

RECENT EXPERIENCES (today's temporal memories, up to 24):
{recent_memories}

EXISTING REFLECTIVE MEMORY (top-8 most relevant):
{existing_reflections}

Instructions
1) Generate UP TO FOUR candidate reflections grounded in explicit evidence from today's experiences. Focus on recurring habits, preferences, constraints (including financial), social tendencies, and evolving beliefs.
2) Each reflection MUST use this fixed schema:
   - "condition":   the context in which the tendency applies (e.g., "after a long workday", "when monthly spending is high")
   - "tendency":    the behavioral tendency itself (e.g., "prefers quiet restaurants")
   - "evidence":    supporting evidence from the day's records (reference specific events)
   - "implication": what this implies for future behavior
3) Compare each candidate against the EXISTING reflective memory:
   - If consistent with an existing reflection, set "action":"consolidate" and reference the matching reflection id in "merge_with"; refine its condition and add the new evidence.
   - If it captures a distinct recurring pattern, set "action":"add".
4) Treat reflections as SOFT tendencies that accumulate gradually, not hard rules. Do not draw strong conclusions from a single isolated event; require recurring evidence before asserting a tendency.
5) Add at most THREE new reflective entries; candidates with limited evidence should be dropped (do not add them as standalone entries).

Output (JSON only; no extra text)
{
  "reflections": [
    {
      "action": "add" | "consolidate",
      "merge_with": "<existing reflection id, or empty>",
      "condition": "<string>",
      "tendency": "<string>",
      "evidence": "<string referencing today's events>",
      "implication": "<string>"
    }
  ]
}
"""
