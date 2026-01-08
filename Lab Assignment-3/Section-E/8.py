#8. Evaluate model using MAE, MSE, RMSE and print all metrics.
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
# Actual vs predicted values
y_true = np.array([3, 5, 7])
y_pred = np.array([2, 5, 9])
MAE = mean_absolute_error(y_true,y_pred)
MSE = mean_squared_error(y_true,y_pred)
RMSE = np.sqrt(MSE)
print("MAE:",MAE)
print("MSE:",MSE)
print("RMSE:",RMSE)
print("Shomya Sarraf,23053668")
