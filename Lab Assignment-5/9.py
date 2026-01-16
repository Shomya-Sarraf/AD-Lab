# 9. Regularization Study
# Train logistic regression with:
# A. No regularization
# B. L1 regularization
# C. L2 regularization
# Compare coefficients and sparsity.
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import numpy as np
X, y = make_classification(
    n_samples=200,
    n_features=5,
    n_informative=3,
    n_redundant=2,
    random_state=42
)
model_none = LogisticRegression(penalty=None, solver='lbfgs', max_iter=500)
model_none.fit(X, y)
model_l1 = LogisticRegression(penalty='l1', solver='liblinear', max_iter=500)
model_l1.fit(X, y)
model_l2 = LogisticRegression(penalty='l2', solver='lbfgs', max_iter=500)
model_l2.fit(X, y)
print("No Regularization Coefficients:\n", model_none.coef_)
print("\nL1 Regularization Coefficients:\n", model_l1.coef_)
print("\nL2 Regularization Coefficients:\n", model_l2.coef_)
print("\nZero coefficients in L1:", np.sum(model_l1.coef_ == 0))
print("Zero coefficients in L2:", np.sum(model_l2.coef_ == 0))
print("Shomya Sarraf , 23053668")
