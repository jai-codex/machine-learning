import seaborn as sns
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. Load dataset
df = sns.load_dataset("titanic")


# 2. Remove unnecessary columns
df = df.drop(["deck", "alive"], axis=1)


# 3. Handle missing values
df["age"] = df["age"].fillna(df["age"].median())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
df["embark_town"] = df["embark_town"].fillna(
    df["embark_town"].mode()[0]
)


# 4. Separate features and target
y = df["survived"]
X = df.drop("survived", axis=1)


# 5. Convert categories to numbers
X = pd.get_dummies(X, drop_first=True)


# 6. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 7. Create model
model = LogisticRegression(max_iter=1000)


# 8. Train model
model.fit(X_train, y_train)


# 9. Make predictions
predictions = model.predict(X_test)


# 10. Check accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)