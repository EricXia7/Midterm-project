import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
from sklearn import linear_model
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D

df11 = pd.read_csv('c:/Users/1Econ/Python/Midterm-project/202211.csv')
print(df11)

X = df11[['dis','score']].values.reshape(-1,2)
Y = df11['price']

x = X[:, 0]
y = X[:, 1]
z = Y


x_pred = np.linspace(6, 24, 30)   # range of porosity values
y_pred = np.linspace(0, 10, 30)  # range of brittleness values
xx_pred, yy_pred = np.meshgrid(x_pred, y_pred)
model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T


ols = linear_model.LinearRegression()
model = ols.fit(X, Y)
predicted = model.predict(model_viz)

r2 = model.score(X, Y)
