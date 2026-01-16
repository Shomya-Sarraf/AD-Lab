# 3. Write a program to classify a new data point using Naïve Bayes given:
# A. Prior probabilities
# B. Conditional probabilities
priors = {'Yes':0.6,'No':0.4}
cond = {
    'Sunny':{'Yes':0.2,'No':0.8},
    'Weak':{'Yes':0.7,'No':0.3}
}
def predict():
    probs = {}
    for c in priors:
        probs[c] = priors[c] * cond['Sunny'][c] * cond['Weak'][c]
    return max(probs, key=probs.get)
print(predict())
print("Shomya Sarraf, 23053668")

