from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
confusion = confusion_matrix(y_test, predictions)

print("Predictions:", predictions)
print("Actual:", y_test)
print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(confusion)