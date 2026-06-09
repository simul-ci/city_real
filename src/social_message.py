SOCIAL_MESSAGE_PROMPT = """Write a short message/discussion with a target friend.

Persona: {gender} {occupation}
Education: {education}
Personality: {personality}
Modality: {mode}         # 'online' or 'offline'
Target: {friend_name} (relationship {relationship_score}/100)
Belief cues (optional): {beliefs}     # e.g., {"affinity":0.7,"trust":0.6,"familiarity":0.8}
Current intention: {intention}
Emotion: {emotion_types}
Thought: {thought}

Previous chat history (optional):
{chat_history}

Constraints
- Output ONLY the message text (no JSON, no quotes).
- ≤ 100 characters.
- Natural, context-appropriate, and aligned with persona & intention.
- Respect modality:
  - online → concise opener or check-in
  - offline → short ask to meet now/soon (place/time optional)
- Avoid links, hashtags, or emojis unless clearly appropriate.
- Apply any discussion guardrails: {discussion_constraint}

Now write the message:
"""
