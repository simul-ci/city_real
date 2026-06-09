# Financial pressure is NOT an LLM prompt. It is a continuous signal computed by a
# deterministic formula and then passed as an input field to the intention, place-selection,
# transport-selection, and stay-home decision prompts (see those files). It is modeled
# separately from the four interrupt-driven needs (hunger, energy, safety, social).
#
# Notation:
#   B_u      : agent u's monthly discretionary budget
#   S_u^t    : cumulative discretionary spending up to time t
#   A_u^t    : remaining available budget = max(B_u - S_u^t, 0)
#   rho_t    : fraction of the month elapsed, in [0, 1]
#   epsilon  : small constant for numerical stability
#
# Financial pressure:
#   p_u^t = clip( S_u^t / (B_u + epsilon) - rho_t , 0, 1 )
#
# Interpretation:
#   - Higher p_u^t  => the agent is spending faster than expected for this point in the month.
#   - Pressure also rises when the remaining budget A_u^t is lower than the expected
#     remaining budget (1 - rho_t) * B_u.
#
# Effect (applied via the prompts that consume {financial_pressure}):
#   Biases the agent toward lower-cost POIs, cheaper transport modes, fewer paid leisure
#   activities, or staying at the current location. It conditions activity choice, destination
#   choice, transport selection, and stay-home decisions, but does NOT directly interrupt
#   ongoing behavior (unlike the four interrupt-driven needs).
