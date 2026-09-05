from sklearn.model_selection import train_test_split

study_hours = [2, 3, 4, 5, 6]
marks = [40, 50, 60, 70, 80]

X_train, X_test, y_train, y_test = train_test_split(
    study_hours,
    marks,
    test_size=0.2,
    random_state=42
)

print("X_train:", X_train)
print("X_test:", X_test)

print("y_train:", y_train)
print("y_test:", y_test)