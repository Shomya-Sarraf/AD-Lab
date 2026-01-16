# 10. Implement train-test split manually and evaluate Naïve Bayes
# performance.
import random
data = list(range(20))
random.shuffle(data)
train = data[:15]
test = data[15:]
print("Train:", train)
print("Test:", test)
print("Shomya Sarraf, 23053668")