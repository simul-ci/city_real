# Adapter edit vocabulary (style axes) used by the alignment analyst.
# Each search action selects ONE target module and up to two axis-direction pairs.
# Every axis also admits a "neutral" direction meaning "leave this axis unchanged".
# Selector features (below) define the agent group an edit applies to.

STYLE_AXES = {
  "daily_structure": {
    "regularity":                ["lower", "neutral", "higher"],
    "wake_shift":                ["earlier", "neutral", "later"],
    "evening_activity_tendency": ["lower", "neutral", "higher"],
    "weekday_rigidity":          ["lower", "neutral", "higher"]
  },
  "intention": {
    "outing_propensity":         ["lower", "neutral", "higher"],
    "locality_preference":       ["lower", "neutral", "higher"],
    "routine_preference":        ["lower", "neutral", "higher"],
    "social_outing_tendency":    ["lower", "neutral", "higher"]
  },
  "trip": {
    "exploration_tendency":      ["lower", "neutral", "higher"],
    "multi_stop_tendency":       ["lower", "neutral", "higher"],
    "familiar_place_preference": ["lower", "neutral", "higher"],
    "destination_range_tendency":["shorter", "neutral", "longer"]
  },
  "vehicle": {
    "walking_preference":        ["lower", "neutral", "higher"],
    "transit_preference":        ["lower", "neutral", "higher"],
    "effort_aversion":           ["lower", "neutral", "higher"],
    "weather_sensitivity":       ["lower", "neutral", "higher"]
  },
  "home_activity": {
    "rest_tendency":             ["lower", "neutral", "higher"],
    "chore_tendency":            ["lower", "neutral", "higher"],
    "hobby_tendency":            ["lower", "neutral", "higher"],
    "family_engagement":         ["lower", "neutral", "higher"]
  }
}

# Selector features used to define the agent group G for an edit:
SELECTOR_FEATURES = [
  "age_bin",
  "occupation_class",
  "household_class",
  "wake_bin_raw",
  "trips_per_day",
  "home_stay_fraction",
  "local_trip_rate",
  "long_trip_rate",
  "mean_log_trip_distance",
  "peak_start_bin"
]

# Soft-tendency policy enforced on rewriter output:
#   - max_words: 80
#   - reject clock times (e.g., 18:30), exact distances (e.g., 2 km), numeric triggers
#   - forbidden patterns: always, never, must, only; explicit if-then rules
