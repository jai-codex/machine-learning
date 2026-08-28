import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [18, 19, 18],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print(df)

data = {
    "Name": ["Jai", "Shree", "Gopi"],
    "Age": [19, 18 , 20],
    "Marks": [99, 100, 98]
}

df = pd.DataFrame(data)
print(df)