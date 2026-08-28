import pandas as pd

df = pd.read_csv("students.csv")
print(df)

print("-------------------")

df["Passed"] = df["Marks"] >= 40
print(df)

print("-------------------")

df["Marks"] = df["Marks"] + 5
print(df)


print("-------------------")

df = df.drop("Passed", axis=1)
print(df)