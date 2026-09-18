import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)

df["MedHouseVal"] = data.target

X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

print("X Head:")
print(X.head())

print("\nX Shape:")
print(X.shape)

print("\ny Head:")
print(y.head())

print("\ny Shape:")
print(y.shape)

