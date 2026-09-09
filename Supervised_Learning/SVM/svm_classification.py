from sklearn.svm import SVC

# Feature: Study Hours
X = [[1], [2], [3], [6], [7], [8]]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

# Create the model
model = SVC()

# Train the model
model.fit(X, y)

# Make a prediction
prediction = model.predict([[4]])

print("Prediction:", prediction[0])