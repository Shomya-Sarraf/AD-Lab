# 5. PCA vs No PCA in Classification
# Train an SVM classifier:

# A. Without PCA
# B. With PCA (k components)
# Compare:
# A. Accuracy
# B. Training time
# C. Overfitting behavior

from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
# Without PCA
start = time.time()
model = SVC().fit(X_train, y_train)
acc1 = accuracy_score(y_test, model.predict(X_test))
time1 = time.time() - start
# With PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)
start = time.time()
model = SVC().fit(X_train_pca, y_train)
acc2 = accuracy_score(y_test, model.predict(X_test_pca))
time2 = time.time() - start
print("Accuracy without PCA:", acc1, "Time:", time1)
print("Accuracy with PCA:", acc2, "Time:", time2)
print("Shomya Sarraf, 23053668")