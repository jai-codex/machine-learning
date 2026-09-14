import pandas as pd
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = sns.load_dataset("titanic")

# Remove unnecessary columns
df = df.drop(["deck", "alive"], axis=1)

# Missing values
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
df["embark_town"] = df["embark_town"].fillna(
    df["embark_town"].mode()[0]
)

# Features and target
y = df["survived"]
X = df.drop("survived", axis=1)

# Encoding
X = pd.get_dummies(X, drop_first=True)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X, y)
prediction = model.predict(X_test)

print("Test Values:", X_test)
print("Prediction:", prediction[:10])
print("Actual Values:", y_test)

accuracy = accuracy_score(y_test, prediction)
print("Accuray:", accuracy)