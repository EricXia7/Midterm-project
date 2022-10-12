import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
from sklearn import linear_model
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D


df11 = pd.read_csv('/Users/brucehu/Desktop/Nov.csv')


plt.style.use('ggplot')
x = df11[['dis','score']]
y = df11['price']
 
regr = linear_model.LinearRegression()
regr.fit(x, y)


# In[6]:


print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)



