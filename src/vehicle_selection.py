VEHICLE_SELECTION_PROMPT = """You are a vehicle selector in an urban simulation. Choose the best travel mode for the next trip.

Trip
- Distance to destination (meters): {distance}
- Expected travel time: {expected_travel_time}
- Time of day: {time_of_day}
- Month: {month}
- Weather: {weather}
- Temperature (°C): {temperature}
- Current location: {current_location}

Agent
- Age: {age}
- Occupation: {occupation}
- Consumption level: {consumption}
- Emotion: {emotion_types}
- Thought: {thought}
- Persona: {persona}
- Financial pressure (0-1, higher = more constrained): {financial_pressure}

Available vehicles (choose only from this list):
{vehicle_list}

Context:
{context}


Decision rules
- Pick exactly ONE mode from {vehicle_list}. Do not invent modes.
- Prioritize: (1) safety & feasibility, (2) on-time arrival given time_budget/urgency, (3) cost given financial pressure (passes/ownership; high pressure favors walking/cycling/cheaper transit), then (4) comfort/habit.
- Long distance or heavy traffic often favors bus/train; short distance favors walk/bicycle if safe and energy allows.
- In poor weather (rain/snow/heat/cold) or at night, avoid unsafe modes (e.g., bicycle) unless clearly acceptable.
- If energy (or another higher-priority need) is below/near its threshold, avoid physically demanding modes.
- If several modes are similar, prefer the safer and cheaper option.

Output (JSON only; no extra text)
{
  "vehicle": "<one of vehicle_list>",
  "reason": "<≤ 25 words referencing key factors (distance/weather/time/availability/needs/cost)>"
}
"""
