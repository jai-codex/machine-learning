import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Rahul", "Amit"],
    "Marks": [80, 90]
})

df2 = pd.DataFrame({
    "Name": ["Sneha", "Riya"],
    "Marks": [75, 85]
})

df = pd.concat([df1, df2], ignore_index=True)

print(df)

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Rahul", "Amit", "Sneha"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [80, 90, 75]
})

result = pd.merge(students, marks, on="ID")

print(result)