# score_processor.py (Local Branch - Non-interactive)

# Predefined array of scores (no user input needed)
scores = [85, 92, 78, 90, 95, 88, 76]

# Calculate all metrics
total_sum = sum(scores)
average = total_sum / len(scores)
max_score = max(scores)
min_score = min(scores)

# Display results
print("=== Score Processing Results ===")
print(f"Scores: {scores}")
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
print(f"Maximum Score: {max_score}")
print(f"Minimum Score: {min_score}")