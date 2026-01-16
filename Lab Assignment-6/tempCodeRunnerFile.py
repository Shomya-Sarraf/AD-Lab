# 5. Given a dataset stored in a CSV file, write a program to:
# A. Read data
# B. Calculate class priors
# C. Apply Naïve Bayes
# D. Predict class labels
import pandas as pd
df = pd.read_csv("data.csv")
classes = df['Class'].unique()
priors = df['Class'].value_counts(normalize=True)
print(priors)
print("Shomya Sarraf, 23053668")