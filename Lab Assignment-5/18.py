# 18. Bias-Variance Tradeoff
# Train models with different regularization strengths and analyze bias and variance.
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X, y = make_classification(n_samples=500, n_features=5,
                           n_informative=3, n_redundant=2,
                           random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
C_values = [0.01, 0.1, 1, 10, 100]
print("C Value | Train Acc | Test Acc")
for C in C_values:
    model = LogisticRegression(C=C, max_iter=500)
    model.fit(X_train, y_train)
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))
    print(C, " | ", round(train_acc, 3), " | ", round(test_acc, 3))
print("Shomya Sarraf , 23053668")
