# 1. Write a Python program to implement Naïve Bayes classifier from
# scratch for a binary classification problem using a small categorical
# dataset.
import pandas as pd
data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong'],
    'Play': ['No','No','Yes','Yes','Yes','No']
}
df = pd.DataFrame(data)
def train_nb(df):
    classes = df['Play'].unique()
    priors = {}
    likelihood = {}
    for c in classes:
        priors[c] = len(df[df['Play']==c]) / len(df)
    for col in df.columns[:-1]:
        likelihood[col] = {}
        for val in df[col].unique():
            likelihood[col][val] = {}
            for c in classes:
                count = len(df[(df[col]==val) & (df['Play']==c)])
                total = len(df[df['Play']==c])
                likelihood[col][val][c] = count / total
    return priors, likelihood
priors, likelihood = train_nb(df)
print(priors)
print(likelihood)
print("Shomya Sarraf, 23053668")