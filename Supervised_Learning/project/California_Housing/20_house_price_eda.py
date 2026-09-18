from sklearn.datasets import fetch_california_housing
import pandas as pd

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)
print(df)

print("First 5 raws:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumes:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistics")
print(df.describe())
