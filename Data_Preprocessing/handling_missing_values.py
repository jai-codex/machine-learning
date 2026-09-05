import pandas as pd

data = {
    "Name": ["Rahul", "Amit", "Sneha"],
    "Age": [18, None, 19],
    "Marks": [80, 90, None]
}

df = pd.DataFrame(data)
print("Original Values:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned values:")
print(df)