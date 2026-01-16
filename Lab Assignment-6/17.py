import math
emails = [
    "win money",
    "cheap offer",
    "meeting today",
    "project work"
]
labels = [
    "spam",
    "spam",
    "ham",
    "ham"
]
vocab = list(set(" ".join(emails).split()))
print("Vocabulary:", vocab)
model = {}
for c in ["spam", "ham"]:
    words = []
    for i in range(len(emails)):
        if labels[i] == c:
            words += emails[i].split()
    total = len(words)
    model[c] = {}
    for w in vocab:
        model[c][w] = (words.count(w) + 1) / (total + len(vocab))
def predict(email):
    spam_score = 0
    ham_score = 0
    for w in email.split():
        if w in vocab:
            spam_score += math.log(model["spam"][w])
            ham_score += math.log(model["ham"][w])
    if spam_score > ham_score:
        return "spam"
    else:
        return "ham"
test_email = "win money"
print("Test Email:", test_email)
print("Prediction:", predict(test_email))
print("Shomya Sarraf, 23053668")