from sklearn.ensemble import RandomForestClassifier

# Feature: Study Hours
X = [[1], [2], [3], [4], [5], [6], [7], [8]]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)
prediction = model.predict([[7]])

print("Prediction:", prediction[0])