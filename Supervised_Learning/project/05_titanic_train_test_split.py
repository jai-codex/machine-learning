import seaborn as sns 
import pandas as pd
from sklearn.model_selection import train_test_split

df = sns.load_dataset("titanic")

# Remove unnecessary columns
df = df.drop(["deck", "alive"], axis=1)

# Handle missing values
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
df["embark_town"] = df["embark_town"].fillna(
    df["embark_town"].mode()[0]
)

# Separate target and features
y = df["survived"]
X = df.drop("survived", axis=1)

# Encoding 
X = pd.get_dummies(X, drop_first=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)