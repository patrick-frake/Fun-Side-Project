# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:01:28 2024

@author: 16096
"""
import pandas as pd

# Summary table

eddie_data = pd.read_csv('eddie.csv')

eddie_data[['Rapper', 'Rank', 'Monthly']].describe()
eddie_data.describe()


import matplotlib.pyplot as plt

# Scatter plot

plt.scatter(eddie_data['Rank'],
            eddie_data['Monthly'])

plt.title('Eddie Ratings With Monthly Listeners (M)')
plt.xlabel('Rank')
plt.ylabel('Monthly Listeners')



# Regression

import statsmodels.api as sm
import numpy as np


X = sm.add_constant(eddie_data['Monthly'])

y = eddie_data['Rank']

model = sm.OLS(y, X).fit()

print(model.summary())

print(eddie_data[['Rank', 'Monthly']].corr())

reg = np.polyfit(eddie_data['Rank'], eddie_data['Monthly'], 1)

trend = np.polyval(reg, eddie_data['Rank'])
plt.plot(eddie_data['Rank'], trend, )






