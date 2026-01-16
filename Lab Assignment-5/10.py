#  10. Class Imbalance Handling
# Train logistic regression on an imbalanced dataset and:
# A. Observe bias in prediction
# B. Apply class weighting
# C. Compare ROC-AUC scores
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report
X, y = make_classification(
    n_samples=500,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    weights=[0.9, 0.1],
    random_state=42
)
model_normal = LogisticRegression()
model_normal.fit(X, y)
y_pred_normal = model_normal.predict(X)
y_prob_normal = model_normal.predict_proba(X)[:,1]
print("Without Class Weighting:")
print(classification_report(y, y_pred_normal))
auc_normal = roc_auc_score(y, y_prob_normal)
print("ROC-AUC:", auc_normal)
model_weighted = LogisticRegression(class_weight='balanced')
model_weighted.fit(X, y)
y_pred_weighted = model_weighted.predict(X)
y_prob_weighted = model_weighted.predict_proba(X)[:,1]
print("\nWith Class Weighting:")
print(classification_report(y, y_pred_weighted))
auc_weighted = roc_auc_score(y, y_prob_weighted)
print("ROC-AUC:", auc_weighted)
print("Shomya Sarraf , 23053668")
