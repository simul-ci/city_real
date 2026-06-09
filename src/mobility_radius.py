radius_prompt = """Decide the maximum travel radius (meters) for the next trip.

Inputs
- Intention: {intention}
- Weather: {weather}
- Temperature: {temperature}
- Emotion: {emotion_types}
- Current thought: {thought}
- Financial pressure (0-1): {financial_pressure}
- Other information:
-------------------------
{other_info}
-------------------------
- Context (optional): {context}

Rules
- Return a single integer between 3000 and 200000 (meters).
- Smaller radius if time budget is short, energy is low, weather/safety is poor, or financial pressure is high.
- Larger radius if emotion is positive, time budget is large, and fast transport is available.

Output (JSON only; no extra text)
{
  "radius": <integer meters>,
  "reason": "<≤20 words>"
}
"""
