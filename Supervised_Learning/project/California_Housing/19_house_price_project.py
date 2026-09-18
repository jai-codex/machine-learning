import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)
df["MedHouseVal"] = data.target

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())