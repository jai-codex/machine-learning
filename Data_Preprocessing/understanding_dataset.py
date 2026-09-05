import pandas as pd

data = {
     "Study_Hours": [5, 7, 3],
    "Marks": [80, 90, 60],
    "Passed": ["Yes", "Yes", "No"]
}

df = pd.DataFrame(data)
print(df)