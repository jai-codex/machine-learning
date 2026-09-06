from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6], [7], [8]]

y = [0, 0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()

model.fit(X, y)

hours = float(input("Enter study hours: "))

prediction = model.predict([[hours]])

if prediction[0] == 1:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")