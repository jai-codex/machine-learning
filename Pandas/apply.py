import pandas as pd

df = pd.read_csv("students.csv")

def check_marks(marks):
    if marks >= 80:
        return "Good"
    else:
        return "Needs improvement"

df["Result"] = df["Marks"].apply(check_marks)

print(df)