from sklearn.linear_model import LogisticRegression

# Feature: Study hours
X = [[1], [2], [3], [4], [5], [6]]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Make a prediction
prediction = model.predict([[5]])

print("Prediction:", prediction[0])