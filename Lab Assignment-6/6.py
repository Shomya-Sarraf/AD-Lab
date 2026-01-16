# 6. Write a Python program to implement Naïve Bayes for text
# classification using word frequencies (no library).
spam = ["buy now", "cheap offer"]
ham = ["hello friend", "see you"]
def word_count(texts):
    wc = {}
    for t in texts:
        for w in t.split():
            wc[w] = wc.get(w,0)+1
    return wc
print(word_count(spam))
print("Shomya Sarraf, 23053668")
