# 3. Train a Logistic Regression model to classify pass/fail from marks.
from sklearn.linear_model import LogisticRegression
import numpy as np
marks = np.array([[10],[20],[30],[40],[50],[60],[70]])
labels = np.array([0,0,0,1,1,1,1])   # 0 = fail, 1 = pass
model = LogisticRegression()
model.fit(marks, labels)
print("Predict for 35 marks:", model.predict([[35]]))
print("Predict for 55 marks:", model.predict([[55]]))
print("Shomya Sarraf,23053668")