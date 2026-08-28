import pandas as pd

df = pd.read_csv("students.csv")

print(df)

print(df[df["Marks"] >= 80])

print("--------------------")

print(df[(df["Marks"] >= 80) & (df["Age"] == 18)])

print("--------------------")

print(df[df["Age"] > 18])