# 20. Write a program to implement Naïve Bayes using k-fold cross-
# Validation.
import math
import random
emails = [
    "win money",
    "cheap offer",
    "free prize",
    "meeting today",
    "project work",
    "see you",
    "win prize",
    "team meeting"
]
labels = ["spam","spam","spam","ham","ham","ham","spam","ham"]
vocab = list(set(" ".join(emails).split()))
def train_nb(train_emails, train_labels):
    model = {}
    for c in ["spam","ham"]:
        words = []
        for i in range(len(train_emails)):
            if train_labels[i] == c:
                words += train_emails[i].split()
        total = len(words)
        model[c] = {}
        for w in vocab:
            model[c][w] = (words.count(w) + 1) / (total + len(vocab))
    return model
def predict(email, model):
    spam_score = 0
    ham_score = 0
    for w in email.split():
        if w in vocab:
            spam_score += math.log(model["spam"][w])
            ham_score += math.log(model["ham"][w])

    return "spam" if spam_score > ham_score else "ham"
k = 4
data = list(zip(emails, labels))
random.shuffle(data)
fold_size = len(data) // k
accuracies = []
for i in range(k):
    test_data = data[i*fold_size:(i+1)*fold_size]
    train_data = data[:i*fold_size] + data[(i+1)*fold_size:]
    train_emails, train_labels = zip(*train_data)
    test_emails, test_labels = zip(*test_data)
    model = train_nb(train_emails, train_labels)
    correct = 0
    for j in range(len(test_emails)):
        pred = predict(test_emails[j], model)
        if pred == test_labels[j]:
            correct += 1
    acc = correct / len(test_emails)
    accuracies.append(acc)
    print(f"Fold {i+1} Accuracy:", acc)
print("\nAverage Accuracy:", sum(accuracies)/k)
print("Shomya Sarraf, 23053668")
