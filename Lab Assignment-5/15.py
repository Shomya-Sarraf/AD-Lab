# 15. Credit Risk Classification
# Train a logistic regression model to classify loan defaulters. Evaluate using precision-recall curve. 
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt
X, y = make_classification(n_samples=500, n_features=5,
                           n_informative=3, n_redundant=2,
                           weights=[0.7, 0.3],   
                           random_state=42)
model = LogisticRegression()
model.fit(X, y)
y_prob = model.predict_proba(X)[:, 1]
precision, recall, _ = precision_recall_curve(y, y_prob)
ap_score = average_precision_score(y, y_prob)
plt.plot(recall, precision, label="AP = " + str(round(ap_score, 2)))
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve for Credit Risk")
plt.legend()
plt.show()
print("Average Precision Score:", ap_score)
print("Shomya Sarraf , 23053668")
