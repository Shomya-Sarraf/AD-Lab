import math
emails = [
    "win money now",
    "cheap offer buy now",
    "free lottery win",
    "meeting today",
    "project discussion",
    "see you tomorrow"
]
labels = ["spam","spam","spam","ham","ham","ham"]
vocab = list(set(" ".join(emails).split()))
classes = set(labels)
model = {}

for c in classes:
    words = " ".join(emails[i] for i in range(len(emails)) if labels[i]==c).split()
    total = len(words)
    model[c] = {w:(words.count(w)+1)/(total+len(vocab)) for w in vocab}
def predict(email):
    scores = {}
    for c in classes:
        scores[c] = 0
        for w in email.split():
            if w in vocab:
                scores[c] += math.log(model[c][w])
    return max(scores, key=scores.get)
tests = ["win free money", "project meeting today"]
for t in tests:
    print(t, "→", predict(t))
print("Shomya Sarraf, 23053668")
