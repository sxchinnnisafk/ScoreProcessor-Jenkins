# A simple score processing script
scores = [85, 92, 78, 90, 95]

# Calculate metrics
total_sum = sum(scores)
average = total_sum / len(scores)
max_score = max(scores)
min_score = min(scores)

# Display results
print(f"Scores: {scores}")
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
print(f"Highest Score: {max_score}")
print(f"Lowest Score: {min_score}")