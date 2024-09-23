import numpy as np


suspect_profile = np.array([0, 1, 1, 0, 2, 2, 1, 0, 1, 0])
crime_scene_profile = np.array([0, 1, 1, 0, 2, 2, 1, 0, 1, 2])


match_count = np.sum(suspect_profile == crime_scene_profile)
total_markers = len(suspect_profile)


match_percentage = (match_count / total_markers) * 100


if match_percentage == 100:
    match_result = "Match: The suspect's DNA matches the crime scene DNA."
else:
    match_result = "No match: The suspect's DNA does not fully match the crime scene DNA."


print("Forensic DNA Profiling Results:")
print(f"Suspect's DNA Profile: {suspect_profile}")
print(f"Crime Scene DNA Profile: {crime_scene_profile}")
print(f"Match Percentage: {match_percentage:.2f}%")
print(match_result)
