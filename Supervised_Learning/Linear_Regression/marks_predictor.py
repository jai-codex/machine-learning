from sklearn.linear_model import LinearRegression

# Study hours
X = [[1], [2], [3], [4], [5]]

# Marks
y = [35, 45, 55, 65, 75]

model = LinearRegression()

model.fit(X,y)
study_hours = int(input("Enter study hours: "))

prediction = model.predict([[study_hours]])
print("Perdicted marks:", prediction[0])