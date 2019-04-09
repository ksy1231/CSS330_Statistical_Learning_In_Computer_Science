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
brozek = raw_data[:,1]
siri = raw_data[:,2]
data = np.concatenate((brozek, siri))

n_group = np.size(brozek) # number of brozeks and number of siris


#- Calculate difference in mean of first and last n_group values for 10000
#  randomizations of data. The first n_group values represents brozek values
#  and the second n_group values represents siri values. Note use of
#  negative index slicing:

results = np.zeros(10000, dtype='d')
for i in range(np.size(results)):
    np.random.shuffle(data)  # done in-place
    results[i] = np.mean(data[:n_group]) - np.mean(data[-n_group:])


#- Calculate and print original data difference in mean of each of the two 
#  algorithms, the p-value for where the absolute value of the difference 
#  is larger than the absolute value of the difference, since we're doing 
#  a two-tailed test:

diff_orig = np.mean(brozek) - np.mean(siri)
p_value_orig = np.sum(np.absolute(results) >= abs(diff_orig)) / \
               np.size(results)
               
#+ The "<" character left justifies in format:
print('Orig. sample difference in mean of ' + \
      'Brozek - mean of Siri: ' + \
      "{:<8.4f}".format(diff_orig))
print('p-value for abs. value of sample difference >= abs. value' + \
      "{:<8.4f}".format(diff_orig) + ': ' + \
      "{:<8.4f}".format(p_value_orig))
      

#- Plot histogram:

num_bins = int(np.sqrt(np.size(results)))   #zyBooks Section 1.3
plt.figure(1)
plt.hist(results, num_bins, normed=True)
plt.ylabel('Pseudo-PDF')
plt.xlabel('Difference in Mean Between Brozek and Siri Algorithms')
plt.title('Randomization Test for Brozek and Siri Algorithms')
plt.savefig('prob01-hist.png')


#===== end file =====