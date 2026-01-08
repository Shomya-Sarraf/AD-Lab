# 7. Perform train-test split manually without using sklearn.
import numpy as np
import pandas as pd
data = pd.DataFrame({
    "X": np.arange(1, 21),      # 20 samples
    "Y": np.arange(21, 41)
})
# Shuffle the rows
data = data.sample(frac=1).reset_index(drop=True)
# 70% train
train_size = int(0.7 * len(data))
train = data.iloc[:train_size]
#30% test
test = data.iloc[train_size:]
print("Training set:\n", train)
print("\nTest set:\n", test)
print("Shomya Sarraf,23053668")

