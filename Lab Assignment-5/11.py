# 11. Threshold Tuning
# Change classification threshold from 0.5 to other values and analyze:
# A. Precision
# B. Recall
# C. Confusion matrix
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score
X, y = make_classification(n_samples=300, n_features=2,
                           n_informative=2, n_redundant=0,
                           random_state=42)
model = LogisticRegression()
model.fit(X, y)
y_prob = model.predict_proba(X)[:, 1]
thresholds = [0.3, 0.5, 0.7]
for t in thresholds:
    print("\nThreshold:", t)
    y_pred = (y_prob >= t).astype(int)
    cm = confusion_matrix(y, y_pred)
    print("Confusion Matrix:\n", cm)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    print("Precision:", precision)
    print("Recall:", recall)
print("Shomya Sarraf , 23053668")
