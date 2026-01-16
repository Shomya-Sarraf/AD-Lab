# 16. Multicollinearity Effect
# Create correlated features and observe how logistic regression coefficients behave.
import numpy as np
from sklearn.linear_model import LogisticRegression
np.random.seed(42)
X1 = np.random.rand(100)
X2 = X1 * 0.95 + 0.05 * np.random.rand(100) 
X = np.column_stack((X1, X2))
y = (X1 > 0.5).astype(int)
model = LogisticRegression()
model.fit(X, y)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Shomya Sarraf , 23053668")
