from sklearn.neighbors import KNeighborsClassifier

# Feature: Study Hours
X = [[1], [2], [3], [7], [8], [9]]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X, y)

# Make prediction
prediction = model.predict([[8]])

print("Prediction:", prediction[0])