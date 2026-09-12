import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")

# Remove unnecessary columns
df = df.drop(["deck", "alive"], axis=1)

# Missing values
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
df["embark_town"] = df["embark_town"].fillna(
    df["embark_town"].mode()[0]
)

# Separate target
y = df["survived"]
X = df.drop("survived", axis=1)

# Convert categorical columns into numbers
X = pd.get_dummies(X, drop_first=True)

print(X.head())
print("\nData types:")
print(X.dtypes)