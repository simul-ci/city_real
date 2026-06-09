orchestrator_prompt = """Your job: look at the full context below and decide how to progress the agent this timestep. The orchestrator is invoked whenever a new decision is required (start or end of an activity, on arrival at a destination, when a need becomes urgent, or when the environment changes).

–––––  CONTEXT  –––––
• Current observation : {observation}
• Schedule status     : {schedule_context}        # ongoing block or EMPTY flexible window
• Active intention    : {active_intention}        # current goal, area anchor, expected duration, status
• Location            : {location}
• Internal state      : {internal_state}          # needs vector, dominant need, fatigue, mood
• Financial pressure  : {financial_pressure}      # 0-1, higher = more constrained
• Retrieved memory    : {memory_slice}            # temporal + reflective insights
• Social context      : {social_context}          # nearby agents, relationships
• Nearby POIs         : {nearby_pois}
• Weather             : {weather}
• Persona snapshot    : {persona_brief}
• Extra context       : {context}

–––––  AVAILABLE BLOCKS  –––––
{block_descriptions}
(If no special action is required, choose "continue_activity".)

## Decide on the active intention
First decide what happens to the current intention:
- "continue" : keep pursuing the same intention with the same area anchor.
- "revise"   : keep the goal but adjust details (e.g., change area, duration, or sub-activity) due to needs, financial pressure, social context, or environment.
- "complete" : the intention has been fulfilled; the agent is ready to move on or return home.
- "replace"  : abandon the current intention for a new one (e.g., an urgent need or scheduled activity takes over).

## Then route to a block
Given the intention action and the dominant need/context, choose the block that best progresses the agent, or "continue_activity" if staying with the current activity is wiser.

## Respond
Return **only** a JSON function call:

{
  "type": "function",
  "function": {
    "name": "select_block",
    "description": "Select the intention action and the block for this timestep",
    "parameters": {
      "type": "object",
      "properties": {
        "intention_action": {
          "type": "string",
          "enum": ["continue", "revise", "complete", "replace"],
          "description": "What to do with the active intention"
        },
        "block_name": {
          "type": "string",
          "enum": ["continue_activity", ...{blocks}],
          "description": "Name of the chosen block"
        },
        "reason": {
          "type": "string",
          "description": "≤ 20-word justification for logging (will not be shown to the LLM again)"
        }
      },
      "required": ["intention_action", "block_name", "reason"]
    }
  }
}

Do **not** output anything else.
"""
