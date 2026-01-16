# 2. Logistic Regression Using scikit-learn
# Load a binary classification dataset and:
# A. Train a Logistic Regression model
# B. Print coefficients and intercept
# C. Predict probabilities and class labels
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
X, y = make_classification(
    n_samples=100,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_repeated=0,
    random_state=42
)
model = LogisticRegression()
model.fit(X, y)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predictions:", model.predict(X[:5]))
print("Probabilities:", model.predict_proba(X[:5]))
print("Shomya Sarraf , 23053668")
