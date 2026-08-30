import pandas as pd

data = {
    "Name": ["Rahul", "Amit", "Sneha", "Riya"],
    "City": ["Pune", "Mumbai", "Pune", "Mumbai"],
    "Marks": [80, 90, 70, 85]
}

df = pd.DataFrame(data)

print(df.groupby("City")["Marks"].mean())
print(df.groupby("City")["Marks"].max())
print(df.groupby("City")["Marks"].min())