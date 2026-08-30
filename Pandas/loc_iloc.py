import pandas as pd

df = pd.read_csv("students.csv")
print(df)

print("--------------")
print(df.iloc[1])
print((df.iloc[0:2]))

print("--------------")
print(df.loc[2])
print(df.loc[:, "Marks"])
