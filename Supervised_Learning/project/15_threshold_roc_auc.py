import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score


# Load dataset
df = sns.load_dataset("titanic")


# Remove unnecessary / leakage columns
df = df.drop(["deck", "alive"], axis=1)


# Features and target
X = df.drop("survived", axis=1)
y = df["survived"]


# Numerical columns
numeric_features = [
    "age",
    "fare",
    "sibsp",
    "parch"
]


# Categorical columns
categorical_features = [
    "sex",
    "embarked",
    "class",
    "who",
    "adult_male",
    "embark_town",
    "alone"
]


# Numerical preprocessing
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])


# Categorical preprocessing
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])


# Combine preprocessing
preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])


# Complete ML pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train
model.fit(X_train, y_train)


# Predict
prediction = model.predict(X_test)


# Evaluate
accuracy = accuracy_score(y_test, prediction)

print("Accuracy:", accuracy)

probabilities = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(y_test, probabilities)

print("ROC-AUC:", auc)

