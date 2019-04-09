#----------------------------------------------------------------------------
# Bootstrap nonparametric method.
#
# Code by Soo Yun Kim
# February 20, 2019
#
# Notes:
# * Written for Python 3.6
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   3.2. 
# * See also James Carpenter and John Bithell, "Bootstrap confidence
#   intervals:  when, which, what?  A practical guide for medical
#   statisticians," Statistics in Medicine, 2000, Vol. 19, pp. 1141-1164
#----------------------------------------------------------------------------


#- Imports:

import numpy as np

#- Data:

raw_data = np.genfromtxt('fat.dat.txt', dtype='d')
age = raw_data[:,4]
older = raw_data[:,1][np.where(age >= 40)]
younger = raw_data[:,1][np.where(age < 40)]


#- Calculate difference for each bootstrap resample the difference in the
#  mean of 40 years and older and younger than 40 years values:

results_older = np.zeros(10000, dtype='d')
results_younger = np.zeros(10000, dtype='d')
for i in range(np.size(results_older)):
    data_older = np.random.choice(older, np.size(older), replace=True)
    data_younger = np.random.choice(younger, np.size(younger), replace=True)
    results_older[i] = np.mean(data_older)
    results_younger[i] = np.mean(data_younger)


#- Calculate and print confidence interval for the method of using "the
#  bootstrap distribution directly to generate the confidence interval.
#  See Carpenter and Bithell, p. 1150 (I did the p-value calculation
#  slightly differently, which is what warrants the abs):

alpha = 0.05
xbar = np.mean(older)
sorted_errors = sorted(results_older - xbar)
error_lower = \
    sorted_errors[int(np.rint(alpha/2.0*np.size(results_older)-1))]
error_upper = \
    sorted_errors[int(np.rint((1.0-alpha/2.0)*np.size(results_older)-1))]
print('bootstrap distrib. direct method confid. interval older: ' + \
      "{:<8.4f}".format(xbar - abs(error_lower)) + ', ' + \
      "{:<8.4f}".format(xbar + error_upper))

alpha = 0.05
xbar = np.mean(younger)
sorted_errors = sorted(results_younger - xbar)
error_lower = \
    sorted_errors[int(np.rint(alpha/2.0*np.size(results_younger)-1))]
error_upper = \
    sorted_errors[int(np.rint((1.0-alpha/2.0)*np.size(results_younger)-1))]
print('bootstrap distrib. direct method confid. interval younger: ' + \
      "{:<8.4f}".format(xbar - abs(error_lower)) + ', ' + \
      "{:<8.4f}".format(xbar + error_upper))
      

#===== end file =====