import seaborn as sns

df = sns.load_dataset("titanic")

print("Before:")
print(df.isnull().sum())

df = df.drop("deck", axis=1)

df["age"] = df["age"].fillna(df["age"].median())
df["embark_town"] = df["embark_town"].fillna(
    df["embark_town"].mode()[0])
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

print("\nAfter:")
print(df.isnull().sum())