# 13. Write a program to compute feature importance from a trained
# Decision Tree.
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier()
model.fit(X, y)
print("Feature Importance:", model.feature_importances_)
print("Shomya Sarraf , 23053668")

