from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

model = DecisionTreeClassifier(max_depth=3)

scores = cross_val_score(model, X, y, cv=5)

print("Scores:", scores)
print("Average Score:", scores.mean())