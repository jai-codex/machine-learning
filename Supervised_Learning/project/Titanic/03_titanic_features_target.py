import seaborn as sns

df = sns.load_dataset("titanic")

# Remove columns we don't want
df = df.drop(["deck", "alive"], axis=1)

# Handle missing values
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
df["embark_town"] = df["embark_town"].fillna(
    df["embark_town"].mode()[0]
)

# Target
y = df["survived"]

# Features
X = df.drop("survived", axis=1)

print("X:")
print(X.head())

print("\ny:")
print(y.head())

print("\nX shape:", X.shape)
print("y shape:", y.shape)