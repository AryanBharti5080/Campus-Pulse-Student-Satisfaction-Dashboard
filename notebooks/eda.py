import pandas as pd

# Load dataset
df = pd.read_csv("data/student_satisfaction.csv")

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check unique values
print("\nUnique values:")
print("Gender:", df["gender"].unique())
print("Year:", df["year"].unique())
print("Department:", df["department"].unique())
print("Facility:", df["facility"].unique())

# Basic statistics
print("\nSummary statistics:")
print(df.describe())

# Average satisfaction score
avg_score = df["satisfaction_score"].mean()
print(f"\nAverage Satisfaction Score: {avg_score:.2f}")

# Average score by facility
print("\nAverage Score by Facility:")
print(df.groupby("facility")["satisfaction_score"].mean())

# Count of responses per facility
print("\nResponses per Facility:")
print(df["facility"].value_counts())