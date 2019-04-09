#------------------------------------------------------------------------------
# Program to solve a cars problem using ANOVA.
#
# Code by Johnny Lin
# January 2019
#
# The null hypothesis is the muA = muB = muC. The alternative hypothesis
# is that at least one pair of mus do not equal. muA is the population mean
# for the Model A number of defects and muB and muC are the same for Models
# B and C, respectively.
#
# Notes:
# * Written for Python 3.6
# * Algorithms based on:  ZyBook, Statistics for Data Analytics, 2016.
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
from scipy.stats import f
import anova_stats         # this is the module I wrote for the ICA


#- Data and parameters:

modelA = np.array([6, 4, 8, 12, 3, 4, 14, 2, 4])  # no. defects for Model A
modelB = np.array([16, 2, 17, 11, 3, 7, 19, 8])   # no. defects for Model B
modelC = np.array([23, 4, 9, 21, 19])             # no. defects for Model C
alpha = 0.05


#- Statistical metrics:
k = 3  # number of levels
n = np.size(modelA) + np.size(modelB) + np.size(modelC)  # total no. samples
dfb = k - 1  # between-group or numerator degrees of freedom
dfw = n - k  # within-group or denominator degrees of freedom
f_statistic = anova_stats.f_statistic([modelA, modelB, modelC])
p_value = 1.0 - f.cdf(f_statistic, dfb, dfw)


#- Print stuff out:

print("f_statistic: " + str(f_statistic))
print("p-value: " + str(p_value))
print("Reject H0?: " + str(p_value < alpha))


#===== end file =====