import pandas as pd

data = {
    "City": ["Pune", "Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)

encoded_data = pd.get_dummies(df, columns=["City"])

print(encoded_data)