import numpy as np

# Case 1: Calculate standard deviation of weekly rainfall data
rainfall = np.array([12, 15, 20, 18, 10, 25, 17])  # sample weekly rainfall data

std_dev = np.std(rainfall)

print("Weekly Rainfall Data:", rainfall)
print("Standard Deviation of Rainfall:", std_dev)


# Case 2: Find mean and median of student exam scores
scores = np.array([78, 85, 90, 66, 88, 72, 95])

mean_score = np.mean(scores)
median_score = np.median(scores)

print("\nStudent Exam Scores:", scores)
print("Mean Score:", mean_score)
print("Median Score:", median_score)


# Scenario: Temperature data analysis
temperature = np.array([30, 32, 31, 29, 35, 33, 34, 28])

mean_temp = np.mean(temperature)
variance_temp = np.var(temperature)
std_temp = np.std(temperature)

print("\nDaily Temperature Data:", temperature)
print("Mean Temperature:", mean_temp)
print("Variance:", variance_temp)
print("Standard Deviation:", std_temp)
