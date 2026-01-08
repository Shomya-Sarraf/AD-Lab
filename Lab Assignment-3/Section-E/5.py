# 5. Train a Decision Tree classifier and print confusion matrix.
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
print("Shomya Sarraf,23053668")