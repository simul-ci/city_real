REWRITER_SYSTEM_PROMPT = """Rewrite one consolidated natural-language soft-tendency adapter for a single simulated agent. The adapter is not a rule or answer key. It competes with the agent's context, needs, preferences, and other motivations. The agent must still make ordinary contextual decisions and retain occasional rare or long-tail behavior. Preserve the persona and keep the tendency specific to the requested target module. Output adapter text only.

Hard constraints (the adapter is rejected and regenerated if it violates any):
- Express SOFT tendencies only (e.g., "tends to", "is somewhat more likely to", "often prefers").
- No absolutist terms: do not use always, never, must, or only.
- No explicit if-then rules or disguised conditions.
- No clock times (e.g., 18:30) and no exact distances (e.g., 2 km, 500 m).
- No hidden numeric parameters or memorized labels.
- Keep it concise (at most ~80 words) and consistent with the agent's persona."""

REWRITER_USER_PROMPT = """Update this agent's soft-tendency adapter to incorporate the requested behavioral edit.

Agent persona: {persona}
Target module: {target}
Behavioral edit (axis -> direction): {delta}
Intent / rationale (gloss): {gloss}
Current adapter (may be empty): {current_adapter}

Write a single short paragraph (1-3 sentences) that:
- Incorporates the requested edit as a soft behavioral tendency for the target module.
- Preserves the agent's existing persona and any compatible prior tendency.
- Biases the agent's decisions without overriding its situational context or internal states.

Output: the adapter text only (no JSON, no quotes, no explanation).
"""

# Retry message appended when validation rejects the output:
REWRITER_RETRY_MESSAGE = """The previous adapter was rejected: {reason}. Rewrite it as a safe soft tendency that avoids clock times, exact distances, absolutist terms (always/never/must/only), and explicit if-then rules."""
