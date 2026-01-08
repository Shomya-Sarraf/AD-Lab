# 5. Draw a heatmap for correlation matrix of a dataset.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = pd.DataFrame({
    "Math": [80, 90, 70, 85, 95],
    "Science": [75, 88, 60, 80, 92],
    "English": [78, 82, 65, 75, 85]
})
corr = data.corr()
sns.heatmap(corr, annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()
print("Shomya Sarraf,23053668")
