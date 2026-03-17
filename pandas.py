import pandas as pd

# Test Case 1: Load COVID-19 dataset and display first 5 records
covid_data = pd.read_csv("covid19.csv")

print("First 5 Records of COVID-19 Dataset:")
print(covid_data.head())


# Test Case 2: Load employee data and summarize statistics
employee_data = pd.read_csv("employee.csv")

print("\nLast 5 Records of Employee Dataset:")
print(employee_data.tail())

print("\nInformation about Employee Dataset:")
print(employee_data.info())

print("\nStatistical Summary of Employee Dataset:")
print(employee_data.describe())
