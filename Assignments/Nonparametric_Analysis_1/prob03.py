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
from scipy.stats import t
import matplotlib.pyplot as plt


#- Data:

raw_data = np.genfromtxt('fat.dat.txt', dtype='d')
age = raw_data[:,4]
older = raw_data[:,1][np.where(age >= 40)]
younger = raw_data[:,1][np.where(age < 40)]


#- Calculate bootstrap resample difference for each bootstrap resample the 
#  difference in the
#  mean of 40 years and older and younger than 40 years values:

results_older = np.zeros(10000, dtype='d')
results_younger = np.zeros(10000, dtype='d')
for i in range(np.size(results_older)):
    data_older = np.random.choice(older, np.size(older), replace=True)
    data_younger = np.random.choice(younger, np.size(younger), replace=True)
    results_older[i] = np.mean(data_older)
    results_younger[i] = np.mean(data_younger)


#- Calcuate and print confidence interval for the "t interval with
#  bootstrap standard error" method:

alpha =  0.05
xbar = np.mean(older)
dof = np.size(older) - 1
t_star_lower = abs(t.ppf(alpha/2.0, dof))
t_star_upper = t.ppf(1.0 - (alpha/2.0), dof)
s_star = np.std(results_older, ddof=1)
print('t interval with SE method confid. interval for older: ' + \
      "{:<8.4f}".format(xbar - (t_star_lower * s_star)) + ', ' + \
      "{:<8.4f}".format(xbar + (t_star_upper * s_star)))

alpha =  0.05
xbar = np.mean(younger)
dof = np.size(younger) - 1
t_star_lower = abs(t.ppf(alpha/2.0, dof))
t_star_upper = t.ppf(1.0 - (alpha/2.0), dof)
s_star = np.std(results_younger, ddof=1)
print('t interval with SE method confid. interval for younger: ' + \
      "{:<8.4f}".format(xbar - (t_star_lower * s_star)) + ', ' + \
      "{:<8.4f}".format(xbar + (t_star_upper * s_star)))
    

#- Plot histogram for older and younger:

#num_bins = int(np.sqrt(np.size(results)))   #zyBooks Section 1.3
plt.figure(1)
#plt.hist(results, num_bins, normed=True)
plt.ylabel('Pseudo-PDF')
plt.xlabel('Percent Body Fat')
plt.title('Randomization Test for Brozek and Siri Algorithms')
plt.savefig('prob03-hist.png')


#===== end file =====