from sklearn.linear_model import LinearRegression

X = [
    [2, 60],
    [3, 70],
    [4, 75],
    [5, 80],
    [6, 90]
]

y = [50, 60, 70, 80, 90]

model = LinearRegression()
model.fit(X,y)

study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))

prediction = model.predict([[study_hours, attendance]])

print("Predicted Marks:", prediction[0])
