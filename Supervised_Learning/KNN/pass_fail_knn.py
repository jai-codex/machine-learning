from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [3], [4], [6], [7], [8], [9]]

y = [0, 0, 0, 0, 1, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

hours = float(input("Enter study hours: "))

prediction = model.predict([[hours]])

if prediction[0] == 1:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")