import pandas as pd

df = pd.read_csv("students.csv")

print("Missing values:")
print(df.isnull().sum())

print("-------------------")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("After filling missing values:")
print(df)