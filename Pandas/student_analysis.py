import pandas as pd

# Read data
df = pd.read_csv("Pandas/students.csv")

# Show data
print("DATA:")
print(df)

print("-------------------")

# Check missing values
print("MISSING VALUES:")
print(df.isnull().sum())

print("-------------------")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("CLEAN DATA:")
print(df)

print("-------------------")

# Basic statistics
print("STATISTICS:")
print(df.describe())

print("-------------------")

# Highest marks
print("HIGHEST MARKS:")
print(df["Marks"].max())

print("-------------------")

# Average marks
print("AVERAGE MARKS:")
print(df["Marks"].mean())

print("-------------------")

# Sort by marks
print("SORTED BY MARKS:")
print(df.sort_values("Marks", ascending=False))

# Save cleaned data
df.to_csv("Pandas/clean_students.csv", index=False)