import pandas as pd

df = pd.read_csv("students.csv")
print(df)

print("\nAfter sorting(small to large):")
print(df.sort_values("Marks"))

print("\nAfter sorting(large to small):")
print(df.sort_values("Marks", ascending=False))