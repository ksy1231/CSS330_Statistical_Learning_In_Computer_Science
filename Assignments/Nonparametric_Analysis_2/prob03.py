#---------------------------------------------------------------------------
# Randomization (i.e., permutation) nonparametric method 
#
# Code by Soo Yun Kim
# February 27, 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   3.2.
#----------------------------------------------------------------------------


#- Imports:

import numpy as np


#- Function to calculate multiple test:

def multiple(x, y, alpha, k, diag=False):
    """Calculate the independent statistical tests 
       using the Randomization (i.e., permutation) nonparametric method.

    Input Parameters:
        x : array
            One sample of data.

        y : array
            Another sample of data.

        alpha : integer
                a significance level
        
        k : integer 
            number of group
        
        diag : boolean
            If True, print out diagnostics.

    Return Parameters:
        p-value.  This is scalar.
    """
    #- Create data array:
    data = np.concatenate((x, y))
    n_group = np.size(x)  #number of x and number of y
    
    
    #- Calculate difference in mean of first and last n_group values for 10000
    #  randomizations of data. The first n_group values represents x values
    #  and the second n_group values represents y values. Note use of negative
    #  index slicing:

    results = np.zeros(10000, dtype='d')
    for i in range(np.size(results)):
        np.random.shuffle(data)  #done in-place
        results[i] = np.mean(data[:n_group]) - np.mean(data[-n_group:])
        
    
    #- Calculate and print original data difference in mean of x and y, the
    #  p-value for where the absolute value of the difference is larger than
    #  the absolute value of the difference, since we're doing:

    diff_orig = np.mean(x) - np.mean(y)
    p_value_orig = np.sum(np.absolute(results) >= abs(diff_orig)) / \
                    np.size(results)

    bonferroni = 1 - (1 - alpha**k)
    
    
    #- Printing diagnostics:

    if diag:
        print('p_value_orig: ' + str(p_value_orig))
        
    return p_value_orig, bonferroni   


if __name__ == "__main__":
    placebo = np.array([6, 4, 2, 2, 1])  
    aspirin = np.array([4, 5, 6, 5, 6])   
    new_painkiller = np.array([6, 5, 7, 8, 7])

    print('p-value for Placebo and Aspirin')
    multiple(placebo, aspirin, 0.1, 3, diag=True)
    print('p-value for Aspirin and New Painkiller')
    multiple(aspirin, new_painkiller, 0.1, 3, diag=True)
    print('p-value for Placebo and New Painkiller')
    multiple(placebo, new_painkiller, 0.1, 3, diag=True)
    print('For overall alpha = 0.1, significant test is: ' + str(0.1/3))


#===== end file =====