from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV


X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

model = DecisionTreeClassifier(random_state=42)

parameter = {
    "max_depth": [2, 3, 4, 5, 6, 7, 8, 9]
}

grid = GridSearchCV(model, parameter, cv=5)
grid.fit(X, y)

print("Best Parameter:", grid.best_params_)
print("Best Score:", grid.best_score_)