# 11. Count word frequency using dictionary.
s="hello My name is Shomya Sarraf"
words=s.split()
freq={}
for w in words:
    if w in freq:
        freq[w]=freq[w]+1
    else:
        freq[w]=1
print(freq)
print("Shomya Sarraf, 23053668")
