#-----------------------------------------------------------------------------
# Program to solve a cars problem using Kruskal-Wallis.
#
# Code by Johnny Lin
# January 2019
#
# The null hypothesis is the muA = muB = muC.  The alternative hypothesis 
# is that at least one pair of mus do not equal.  muA is the population mean 
# for the Model A number of defects and muB and muC are the same for Models
# B and C, respectively.  The null hypothesis is not rejected.
#
# Notes:
# * Written for Python 3.6.
# * Algorithms based on:  ZyBook, Statistics for Data Analytics, 2016.
#-----------------------------------------------------------------------------


#- Imports:

import numpy as np
from scipy.stats import kruskal
from scipy.stats import chi2


#- Data and parameters:

modelA = np.array([6, 4, 8, 12, 3, 4, 14, 2, 4])  #no. defects for Model A
modelB = np.array([16, 2, 17, 11, 3, 7, 19, 8])   #no. defects for Model B
modelC = np.array([23, 4, 9, 21, 19])             #no. defects for Model C
alpha = 0.05

A = np.array([6.2, 2.4, 3.2, 1.9, 0.8])
B = np.array([3.5, 4.7, 5.6, 2.1, 3.2])
C = np.array([6.2, 5.0, 6.9, 7.2, 8.5])

#- Statistical metrics:

g = 3       #number of groups
df = g - 1  #degrees of freedom
#h_statistic, scipy_p_value = kruskal(modelA, modelB, modelC)
h_statistic, scipy_p_value = kruskal(A, B, C)
my_p_value = 1.0 - chi2.cdf(h_statistic, df)


#- Print stuff out:

print("H-statistic: " + str(h_statistic))
print("SciPy kruskal p-value: " + str(scipy_p_value))
print("My p-value: " + str(my_p_value))
print("Reject H0?: " + str(scipy_p_value < alpha))


#===== end file =====