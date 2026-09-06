from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = [
    [2, 60],
    [3, 70],
    [4, 75],
    [5, 80],
    [6, 90],
    [7, 85],
    [8, 95],
    [9, 90],
    [10, 98],
    [11, 97]
]

y = [50, 60, 70, 80, 90, 85, 95, 92, 100, 98]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("X test:", X_test)
print("Predictions:", predictions)
print("Actual Values:", y_test)