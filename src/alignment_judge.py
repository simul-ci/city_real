JUDGE_SYSTEM_PROMPT = """Review a proposed learned adapter for an LLM-agent simulation. Approve only a natural-language soft tendency that competes with context and preserves occasional long-tail behavior. Reject hard rules, disguised conditions, exact answers, memorized labels, item-specific instructions, hidden numeric parameters, persona corruption, and irrelevant text. Return JSON only: {"approved": boolean, "reasons": [string]}."""

JUDGE_USER_PROMPT = """Decide whether the proposed adapter is an acceptable soft behavioral tendency.

Proposed adapter: {proposed_adapter}
Current adapter (may be empty): {current_adapter}
Requested action:
- target module: {target}
- edit (axis -> direction): {delta}
- gloss: {gloss}
Agent context (redacted): {allowed_agent_context}
Policy:
- max words: {max_words}
- forbidden patterns: {forbidden_patterns}

Approve only if ALL hold:
- It expresses a soft tendency, not a hard rule (no always/never/must/only, no if-then).
- It contains no clock times, exact distances, or hidden numeric parameters.
- It preserves the persona and stays relevant to the target module.
- It does not encode exact answers, memorized labels, or item-specific instructions.
- It leaves room for ordinary contextual decisions and occasional long-tail behavior.

Output (JSON only; no extra text)
{
  "approved": <true|false>,
  "reasons": ["<short reason>", "..."]
}
"""
