from sklearn.tree import DecisionTreeClassifier

# Feature: Study Hours
X = [[1], [2], [3], [4], [5], [6], [7], [8]]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)
prediction = model.predict([[6]])

print("Prediction:", prediction[0])
