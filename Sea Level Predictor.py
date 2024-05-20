#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def draw_plot():
    
    timespan = np.arange(1880, 2051, 1)
    timespan_2 = np.arange(2000, 2051, 1)
    
    
    
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    data_cleaned = data.drop(data.index[134])
    data_cleaned_2000 = data.drop(data.index[0:121])
    data_2000 = data_cleaned_2000.drop(data_cleaned_2000.index[13])
    
    x = data_cleaned['Year']
    y = data_cleaned['CSIRO Adjusted Sea Level']
    x_2000 = data_2000['Year']
    y_2000 = data_2000['CSIRO Adjusted Sea Level']
    
    print(x)
    print(y)
    

    # Create scatter plot
    plt.figure(figsize = (10,6))
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, r, p, se = stats.linregress(x, y)
    
    slope_2000, intercept_2000, r_2000, p_2000, se_2000 = stats.linregress(x_2000, y_2000)
    

    plt.plot(timespan, slope * timespan + intercept, 'r', label = 'Regression')
    

    # Create second line of best fit
    plt.plot(timespan_2, slope_2000*timespan_2 + intercept_2000, 'r', label = "Regression from 2000", color = 'green')
    

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()


# In[ ]:




