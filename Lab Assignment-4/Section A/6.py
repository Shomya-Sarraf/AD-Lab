# 6. Analyze the sensitivity of OLS to outliers using leverage and Cook’s distance.
import numpy as np
import statsmodels.api as sm
x = np.array([1,2,3,4,20])
y = np.array([2,4,6,8,100])
X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
print("Cook's distance:", model.get_influence().cooks_distance[0])
print("Shomya Sarraf, 23053668")