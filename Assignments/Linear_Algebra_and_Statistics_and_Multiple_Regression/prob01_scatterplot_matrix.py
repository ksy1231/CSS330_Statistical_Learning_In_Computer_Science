#------------------------------------------------------------------------------
# Problem 1
# Using matplotlib, draw the R-Practice 6.1.1 scatterplot matrix.  Do not use a 
# pre-written scatterplot matrix function such as is provided in matplotlib, 
# pandas, or the seaborn package.  You'll probably find the subplots function 
# to be of use. 
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplots
#
# Code by Soo Yun Kim
# March 13, 2019
#
# Notes:
# * Written for Python 3.4.
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
import matplotlib.pyplot as plt


#- Data: Y, X1, X2, and X3 should all have the same number of elements:

#+ Body fat (%):
Y = np.array([11.9, 22.8, 18.7, 20.1, 12.9, 21.7, 27.1, 25.4, 21.3, 19.3, 
              25.4, 27.2, 11.7, 17.8, 12.8, 23.9, 22.6, 25.4, 14.8, 21.1])

#+ Triceps skinfold thickness (mm):
X1 = np.array([19.5, 24.7, 30.7, 29.8, 19.1, 25.6, 31.4, 27.9, 22.1, 25.5, 
                 31.1, 30.4, 18.7, 19.7, 14.6, 29.5, 27.7, 30.2, 22.7, 25.2])

#+ Midarm circumference (cm)
X2 = np.array([29.1, 28.2, 37, 31.1, 30.9, 23.7, 27.6, 30.6, 23.2, 24.8, 
               30, 28.3, 23, 28.6, 21.3, 30.1, 25.7, 24.6, 27.1, 27.5])

#+ Thigh circumference (cm)
X3 = np.array([43.1, 49.8, 51.9, 54.3, 42.2, 53.9, 58.5, 52.1, 49.9, 53.5, 
               56.6, 56.7, 46.5, 44.2, 42.7, 54.4, 55.3, 58.6, 48.2, 51])

X = np.hstack((np.vstack(X1), np.vstack(X2), np.vstack(X3)))

num_var = np.shape(X)[1]

#- Make subplots:

fig, axes = plt.subplots(num_var, num_var)
diag = ['Y', 'X1', 'X2', 'X3']

for i in np.arange(num_var):
    for j in np.arange(num_var):
        if i == j:
            axes[i,j].set_xticks([])
            axes[i,j].set_yticks([])
            axes[i,j].text(0.5, 0.5, diag[i], fontsize=18,
                horixontalalignment='center', verticalalignment='center',
                transform=axes[i,j].transAxes)
        else:
            axes[i,j].scatter(X[:,j], X[:,i],s=3)
    
    if i != 0: axes[i,j].set_yticks([])
    if j != 0: axes[i,j].set_xticks([])
            
plt.savefig('scatterplot_matrix.png')


#===== end file =====