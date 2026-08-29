import pandas as pd

df = pd.read_csv("students.csv")

print(df)

print("-------------------")

print("First row:\n", df.head(1))

print("-------------------")

print("Last row:\n", df.tail(1))

print("-------------------")

print("Shape:", df.shape)

print("-------------------")

print("Marks:\n", df["Marks"])

print("-------------------")

print("Average marks:", df["Marks"].mean())

print("-------------------")

print("Highest marks:", df["Marks"].max())

print("-------------------")

print("Name and Marks:\n", df[["Name", "Marks"]])

print("-------------------")

df.to_csv("pandas/new_students.csv", index=False)