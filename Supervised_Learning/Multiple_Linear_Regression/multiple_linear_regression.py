from sklearn.linear_model import LinearRegression

# Features: Study Hours, Attendance
X = [
    [2, 60],
    [3, 70],
    [4, 75],
    [5, 80],
    [6, 90]
]

# Target: Marks
y = [50, 60, 70, 80, 90]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[7, 95]])
print("Predicted Marks:", prediction[0])