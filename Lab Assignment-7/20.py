# 20. Implement SVM with RBF kernel and compare it with linear kernel.
from sklearn.svm import SVC
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
model = SVC(kernel="rbf")
model.fit(X, y)
print("RBF SVM trained")
print("Shomya Sarraf , 23053668")
