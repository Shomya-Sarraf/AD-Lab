# 9. Write a program to compute accuracy, precision, recall, and F1-score
# for Naïve Bayes predictions.
TP,FP,FN,TN = 8,2,1,9
accuracy = (TP+TN)/(TP+FP+FN+TN)
precision = TP/(TP+FP)
recall = TP/(TP+FN)
f1 = 2*(precision*recall)/(precision+recall)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)
print("Shomya Sarraf, 23053668")