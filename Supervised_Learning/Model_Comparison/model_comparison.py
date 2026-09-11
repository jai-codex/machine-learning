from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [0, 0, 0, 0, 0,
     1, 1, 1, 1, 1]

models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(max_depth=3),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "SVM": SVC()
}

for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5)
    print(name, ":", scores.mean())