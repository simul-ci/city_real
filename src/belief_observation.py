BELIEF_OBSERVATION_PROMPT = """You are a belief inference module for a human-like agent.
The agent just visited a place and the experience was logged as follows:

Place: {place_name}
POI Description: {poi_description}
Time of Visit: {time_of_day}

Agent Profile:
- Gender: {gender}
- Education Level: {education}
- Consumption Level: {consumption}
- Occupation: {occupation}
- Age: {age}
- Monthly Income: {income}

Agent Context:
- Current Position: {position}
- Ongoing Activity: {activity}
- Emotional State: {emotion}
- Satisfaction Before Visit: {satisfaction}
- Recent Places Visited: {last_visited_entities}

Observations at this place:
- Amount Paid: {cost_paid} yen
- Wait Time: {wait_time} minutes
- Perceived Ambience: {ambience_desc}
- Outcome vs Expectation: {satisfaction_desc}

Based on this single visit, infer your subjective observation for this place on four dimensions in [0,1], where higher is better:
- affordability  (price satisfaction / value; higher = cheaper/better value than expected)
- convenience    (ease of access and use)
- crowding       (higher = more comfortable / less crowded than expected)
- enjoyment      (overall satisfaction with the experience)

Respond in JSON only (no extra text), round to 3 decimals, e.g.:
{
  "affordability": 0.600,
  "convenience": 0.400,
  "crowding": 0.700,
  "enjoyment": 0.750
}
"""
