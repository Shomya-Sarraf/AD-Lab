# 13. Implement Multinomial Naïve Bayes for document classification.
import math
documents = [
    "good movie nice story",
    "excellent film good acting",
    "bad movie boring",
    "worst film terrible",
    "nice good fun movie",
    "awful boring film"
]
labels = ["pos", "pos", "neg", "neg", "pos", "neg"]
def build_vocab(docs):
    vocab = set()
    for doc in docs:
        for word in doc.split():
            vocab.add(word)
    return list(vocab)
vocab = build_vocab(documents)
def word_counts(docs, labels, target_class, vocab):
    counts = {word: 0 for word in vocab}
    for i in range(len(docs)):
        if labels[i] == target_class:
            for word in docs[i].split():
                counts[word] += 1
    return counts
classes = set(labels)
total_docs = len(labels)
priors = {}
likelihood = {}
for c in classes:
    priors[c] = labels.count(c) / total_docs
    wc = word_counts(documents, labels, c, vocab)
    total_words = sum(wc.values())
    likelihood[c] = {}
    for word in vocab:
        likelihood[c][word] = (wc[word] + 1) / (total_words + len(vocab))
def predict(document):
    scores = {}
    for c in classes:
        scores[c] = math.log(priors[c])
        for word in document.split():
            if word in vocab:
                scores[c] += math.log(likelihood[c][word])
    return max(scores, key=scores.get)
test_docs = [
    "good fun movie",
    "boring terrible film",
    "nice acting story",
    "awful bad movie"
]
for doc in test_docs:
    print("Document:", doc)
    print("Predicted Class:", predict(doc))
print("Shomya Sarraf, 23053668")
