#  12. ROC Curve & AUC
# Plot ROC curve and compute AUC for logistic regression. Explain why AUC is preferred over accuracy.
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
X, y = make_classification(n_samples=300, n_features=2,
                           n_informative=2, n_redundant=0,
                           random_state=42)
model = LogisticRegression()
model.fit(X, y)
y_prob = model.predict_proba(X)[:, 1]
fpr, tpr, _ = roc_curve(y, y_prob)
auc = roc_auc_score(y, y_prob)
plt.plot(fpr, tpr, label="AUC = " + str(round(auc, 2)))
plt.plot([0,1], [0,1], linestyle="--")  
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
print("AUC Score:", auc)
print("Shomya Sarraf , 23053668")
