#---------------------------------------------------------------------------
# Randomization (i.e., permutation) nonparametric method.
#
# Code by Soo Yun Kim
# February 20, 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   3.2. 
#----------------------------------------------------------------------------


#- Imports:

import numpy as np
import matplotlib.pyplot as plt

#- Data:

raw_data = np.genfromtxt('fat.dat.txt', dtype='d')
age = raw_data[:,4]
older = raw_data[:,1][np.where(age >= 40)]
younger = raw_data[:,1][np.where(age < 40)]
#older40 = raw_data[:, [1]][data[:,4] >= 40]
#older = older40.ravel()
#younger40 = data[:, [1]][data[:,4] < 40]
#younger = younger40.ravel()
data = np.concatenate((older, younger))

n_older = np.size(older) #number of older values


#- Calculate difference in mean of first and last n_group values for 10000
#  randomizations of data. The first n_group values represents 40 years and 
#  older values and the second n_group values represents younger than 40 
#  years values. Note use of negative index slicing:

results = np.zeros(10000, dtype='d')
for i in range(np.size(results)):
    np.random.shuffle(data)  # done in-place
    results[i] = np.mean(data[:n_older]) - np.mean(data[n_older:])


#- Calculate and print original data difference in mean of 40 years and 
#  older and younger than 40 years, the p-value for where the absolute value 
#  of the difference is larger than the absolute value of the difference, 
#  since we're doing:

diff_orig = np.mean(older) - np.mean(younger)
p_value_orig = np.sum(np.absolute(results) >= abs(diff_orig)) / \
               np.size(results)
print('''Orig. sample difference in mean of 40 years and older - mean of 
      younger than 40 years: ''' + str(diff_orig))
print('p-value for sample difference >= ' + str(diff_orig) + ': ' + \
      str(p_value_orig))


#- Plot histogram:

num_bins = int(np.sqrt(np.size(results)))   #zyBooks Section 1.3
plt.figure(1)
plt.hist(results, num_bins, normed=True)
plt.ylabel('Pseudo-PDF')
plt.xlabel('Difference in Mean Between 40 and over and Younger Men')
plt.title('Randomization Test for Brozek and Siri Algorithms')
plt.savefig('prob02-hist.png')


#===== end file =====