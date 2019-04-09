#------------------------------------------------------------------------------
# Program to solve a cars problem using an unpaired two-sample t-test.
#
# Code by Johnny Lin
# January 2019
#
# The null hypothesis is the muA = muB. The alternative hypothesis is that
# muA does not equal muB, where muA is the population mean for the Model A
# number of defects and muB is the same for Model B.
#
# Notes:
# * Written for Python 3. 6.
# * Algorithms based on: ZyBook, Statistics for Data Analytics, 2016.
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
from scipy.stats import t


#- Data and parameters:
modelA = [6, 4, 8, 12, 3, 4, 14, 2, 4]  # number of defects for Model A
modelB = [16, 2, 17, 11, 3, 7, 19, 8]   # number of defects for Model B

xbarA = np.mean(modelA)
xbarB = np.mean(modelB)
sA = np.std(modelA, ddof=1)
sB = np.std(modelB, ddof=1)
nA = len(modelA)
nB = len(modelB)
dof = nA + nB - 2
alpha = 0.05


#- Statistical metrics:  The t-statistic is obtained using the CDF:

t_statistic = (xbarA - xbarB) / np.sqrt((sA**2/nA) + (sB**2/nB))
p_value = t.cdf(t_statistic, dof) * 2.0


#- Print stuff out:

print("Means: " + str(xbarA) + ', ' + str(xbarB))
print("Std. devs,: " + str(sA) + ', ' + str(sB))
print("T-statistic: " + str(t_statistic))
print("p-value: " + str(p_value))
print("Reject H0?: " + str(p_value < alpha))


#===== end file =====