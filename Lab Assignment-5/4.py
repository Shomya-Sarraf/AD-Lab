# 4. Decision Boundary Visualization
# Train a logistic regression model on a 2-feature dataset and:
# A. Plot the decision boundary
# B. Mark misclassified points
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import numpy as np
X, y = make_classification(n_samples=100, 
                           n_features=2, 
                           n_informative=2, 
                           n_redundant=0, 
                           n_repeated=0, 
                           random_state=1)
model = LogisticRegression()
model.fit(X, y)
y_pred = model.predict(X)
plt.scatter(X[:,0], X[:,1], c=y)
wrong = y != y_pred
plt.scatter(X[wrong,0], X[wrong,1], 
            facecolors='none', edgecolors='black', s=100)
x_vals = np.linspace(X[:,0].min(), X[:,0].max(), 100)
y_vals = -(model.coef_[0][0]*x_vals + model.intercept_) / model.coef_[0][1]
plt.plot(x_vals, y_vals)
plt.title("Decision Boundary")
plt.show()
print("Shomya Sarraf , 23053668")
