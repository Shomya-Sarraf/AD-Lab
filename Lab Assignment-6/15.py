import math
docs = ["good movie", "bad movie", "nice film", "boring film"]
labels = ["pos","neg","pos","neg"]
vocab = list(set(" ".join(docs).split()))
classes = set(labels)
multi = {}
for c in classes:
    words = " ".join(docs[i] for i in range(len(docs)) if labels[i]==c).split()
    total = len(words)
    multi[c] = {w:(words.count(w)+1)/(total+len(vocab)) for w in vocab}
bern = {}
for c in classes:
    class_docs = [docs[i] for i in range(len(docs)) if labels[i]==c]
    bern[c] = {w:(sum(w in d for d in class_docs)+1)/(len(class_docs)+2) for w in vocab}
def predict_multi(doc):
    return max(classes, key=lambda c: sum(math.log(multi[c].get(w,1)) for w in doc.split()))
def predict_bern(doc):
    return max(classes, key=lambda c: sum(math.log(bern[c][w] if w in doc else 1-bern[c][w]) for w in vocab))
test = "good film"
print("Multinomial:", predict_multi(test))
print("Bernoulli :", predict_bern(test))
print("Shomya Sarraf, 23053668")
