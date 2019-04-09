#---------------------------------------------------------------------------
# Randomization (i.e., permutation) nonparametric method using image
# classification data.
#
# Code by Johnny Lin
# January-February 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   3.2.  This data in this problem is fake.
#----------------------------------------------------------------------------

#- Imports:

import numpy as np
import matplotlib.pyplot as plt

#- Data:

alg_a = np.array([0.8, 0.9, 0.89, 0.78, 0.91, 0.85, 0.75, 0.8], dtype='d')
alg_b = np.array([0.6, 0.8, 0.74, 0.61, 0.99, 0.68, 0.78, 0.82], dtype='d')
data = np.concatenate((alg_a, alg_b))

n_group = np.size(alg_a)  #number of alg_a and number of alg_b


#- Calculate difference in mean of first and last n_group values for 10000
#  randomizations of data. The first n_group values represents alg_a values
#  and the second n_group values represents alg_b values. Note use of
#  negative index slicing:

results = np.zeros(10000, dtype='d')
for i in range(np.size(results)):
    np.random.shuffle(data)  #done in-place
    results[i] = np.mean(data[:n_group]) - np.mean(data[-n_group:])


#- Calculate and print original data difference in mean of Algorithm A and 
#  Algorithm B, the p-value for where the absolute value of the difference 
#  is larger than the absolute value of the difference, since we're doing
#  :

diff_orig = np.mean(alg_a) - np.mean(alg_b)
p_value_orig = np.sum(np.absolute(results) >= abs(diff_orig)) / \
               np.size(results)

#+ The "<" character left justifies in format:
print('Orig. sample difference in mean of ' + \
      'Algorithm A - mean of Algorithm B: ' + \
      "{:<8.4f}".format(diff_orig))
print('p-value for abs. value of sample difference >= abs. value ' + \
      "{:<8.4f}".format(diff_orig) + ': ' + \
      "{:<8.4f}".format(p_value_orig))
        
        
#- Plot histogram:

num_bins = int(np.sqrt(np.size(results)))   #zyBooks Section 1.3
plt.figure(1)
plt.hist(results, num_bins, normed=True)
plt.ylabel('PDF')
plt.xlabel('Difference in Mean Between Algorithm A and B')
plt.title('Randomization Test for Images Classification')
plt.savefig('randomization-images.png')


#===== end file =====