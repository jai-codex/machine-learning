from sklearn.naive_bayes import GaussianNB

X = [
    [1, 50],
    [2, 55],
    [3, 60],
    [4, 65],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1]

model = GaussianNB()

model.fit(X, y)

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance: "))

prediction = model.predict([[hours, attendance]])

if prediction[0] == 1:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")