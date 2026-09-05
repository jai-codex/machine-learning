from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_test, y_test)

predictions = model.predict(X_test)

print(X_test)
print("Perdictions:", predictions)
print("Actual Values:", y_test)