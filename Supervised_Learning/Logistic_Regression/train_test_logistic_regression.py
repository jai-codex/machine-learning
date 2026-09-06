from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict using test data
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual values:", y_test)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)