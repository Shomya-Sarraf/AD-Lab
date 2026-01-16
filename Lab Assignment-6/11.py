# 11. Write a program to display the confusion matrix for Naïve Bayes
# classifier.
# Confusion Matrix values
TP = 8  
FP = 2   
FN = 1   
TN = 9   
conf_matrix = [
    [TP, FP],
    [FN, TN]
]
print("Confusion Matrix:")
print("Predicted +   Predicted -")
print("Actual +   ", conf_matrix[0])
print("Actual -   ", conf_matrix[1])
accuracy = (TP + TN) / (TP + FP + FN + TN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * (precision * recall) / (precision + recall)
print("\nPerformance Metrics:")
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1-score :", f1)
print("Shomya Sarraf, 23053668")

