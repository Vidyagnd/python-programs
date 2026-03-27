import pandas as pd

# Sample HR dataset
data = {
    'Name': ['A', 'B', 'C', 'C'],
    'Salary': [50000, None, 60000, 60000],
    'Score': [80, None, 75, 75],
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-03-01']
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# 1. Handle missing values (replace with mean)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Score'].fillna(df['Score'].mean(), inplace=True)

# 2. Remove duplicate records
df = df.drop_duplicates()

# 3. Transform data (convert Date column to datetime)
df['Date'] = pd.to_datetime(df['Date'])

print("\nCleaned & Transformed Data:\n", df)
