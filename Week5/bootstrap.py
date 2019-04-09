#----------------------------------------------------------------------------
# Bootstrap nonparametric method.
#
# Code by Johnny Lin
# January 2019
#
# Notes:
# * Written for Python 3.6
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   3.2.  This is a Python version of the R-Practice 3.2.2 in this section.
# * See also James Carpenter and John Bithell, "Bootstrap confidence
#   intervals:  when, which, what?  A practical guide for medical
#   statisticians," Statistics in Medicine, 2000, Vol. 19, pp. 1141-1164
#----------------------------------------------------------------------------


#- Imports:

import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt


#- Data:

male = np.array([245,200,145,180,250,205,195,170,140,170], dtype='d')
female = np.array([165,120,170,190,195,120,170,140,130,150], dtype='d')


#- Calculate difference for each bootstrap resample the difference in the
#  mean of male and female values:

results = np.zeros(10000, dtype='d')
for i in range(np.size(results)):
    data_male = np.random.choice(male, np.size(male), replace=True)
    data_female = np.random.choice(female, np.size(female), replace=True)
    results[i] = np.mean(data_male) - np.mean(data_female)
    
    
#- Plot histogram:

xbar = np.mean(male) - np.mean(female)  #difference in sample means
num_bins = int(np.sqrt(np.size(results)))  #ZyBooks Section 1.3
plt.figure(1)
n, bins, patches = plt.hist(results, num_bins, normed=True)
plt.plot([xbar, xbar], [0, np.max(n)], 'o-')  #plot xbar on distribution
plt.ylabel('PDF')
plt.xlabel('Difference in mean Weight Between Men and Wom [1bs]')
plt.title('Bootstrap Test')
plt.savefig('bootstrap_3_2_2.png')


#- Calcuate and print confidence interval for the "t interval with
#  bootstrap standard error" method:

alpha =  0.05
xbar = np.mean(male) - np.mean(female)
dof = np.size(male) - 1
t_star_lower = abs(t.ppf(alpha/2.0, dof))
t_star_upper = t.ppf(1.0 - (alpha/2.0), dof)
s_star = np.std(results, ddof=1)
print('t interval with SE method confid. interval lower bound: ' + \
      str(xbar - (t_star_lower * s_star)))
print('t interval with SE method confid. interval upper bound: ' + \
      str(xbar + (t_star_upper *s_star)))
      
      
#- Calculate and print confidence interval for the method of using "the
#  bootstrap distribution directly to generate the confidence interval.
#  See Carpenter and Bithell, p. 1150 (I did the p-value calculation
#  slightly differently, which is what warrants the abs):

alpha = 0.05
xbar = np.mean(male) - np.mean(female)
sorted_errors = sorted(results - xbar)
error_lower = sorted_errors[int(np.rint(alpha/2.0*np.size(results)-1))]
error_upper = sorted_errors[int(np.rint((1.0-alpha/2.0)*np.size(results)-1))]
print('bootstrap distrib. direct method confid. interval lower bound: ' + \
      str(xbar - abs(error_lower)))
print('bootstrap distrib. direct method confid. interval upper bound: ' + \
      str(xbar + abs(error_upper)))
      

#===== end file =====