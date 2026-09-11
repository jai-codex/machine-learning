import pandas as pd

data = {
    "math": [80, 70, 90],
    "science": [75, 85, 95]
}

df = pd.DataFrame(data)

df["total_marks"] = df["math"] + df["science"]

print(df)