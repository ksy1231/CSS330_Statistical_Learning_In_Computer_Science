#------------------------------------------------------------------------------
# Randomization (i.e., permutation) nonparametric method.
#
# Code by Johnny Lin
# January 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   3.2.  This is a Python version of the R-Practice 3.2.1 in this section.
#-----------------------------------------------------------------------------

 
#- Imports:

import numpy as np
import matplotlib.pyplot as plt

#- Data:

male = np.array([245,200,145,180,250,205,195,170,140,170], dtype='d')
female = np.array([165,120,170,190,195,120,170,140,130,150], dtype='d')
data = np.concatenate((male, female))

n_group = np.size(male)  # number of males and number of females

#- Calculate difference in mean of first and last n_group values for 10000
#  randomizations of data.  The first n_group values represents male values
#  and the second n_group values represents female values.  Note use of
#  negative index slicing:

results = np.zeros(10000, dtype='d')
for i in range(np.size(results)):
    np.random.shuffle(data)  # done in-place
    results[i] = np.mean(data[:n_group]) - np.mean(data[-n_group:])
    
    
#- Calculate and print p-value as in R-Practice 3.2.1:

p_value = np.sum(results >= 0.0) / np.size(results)
print('p-value for mean of men greater than mean of women: ' + str(p_value))


#- Calculate and print original data difference in mean of men and women,
#  the p-value for where the difference is larger than that difference:

diff_orig = np.mean(male) - np.mean(female)
p_value_orig = np.sum(results >= diff_orig) / np.size(results)
print('Orig. sample difference in mean of men - mean of women: ' + \
      str(diff_orig))
print('p-value for sample difference >= ' + str(diff_orig) + ': ' + \
      str(p_value_orig))



#- Plot histogram:

num_bins = int(np.sqrt(np.size(results)))  # ZyBooks Section 1.3
plt.figure(1)
plt.hist(results, num_bins, normed=True)
plt.ylabel('PDF')
plt.xlabel('Difference in Mean Weight Between Men and Women [lbs]')
plt.title('Randomization (Permutation) Test')
plt.savefig('randomization_3_2_1.png')


#===== end file =====